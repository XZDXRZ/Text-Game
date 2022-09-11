"""This file define the battle function.
"""

from typing import List
import organism
import player
from random import random

DODGE_RATE = .05

def abs(x:float
) -> float:
    """Return the absolute value of input.
    """
    if x >= 0:
        return x
    else:
        return -x

def calc_dodge_possibility(player_speed:int,
                           enemy_speed:int
) -> float:
    """Calculate the probability of dodging.

    Args:
        player_speed: Player speed.
        enemy_speed: The speed of enemy which the player has chosen.
    
    Returns:
        A float represents the probability of dodging.
    """
    return abs(player_speed * 1. - enemy_speed * 1.) * DODGE_RATE

def battle(player_object: player.Player,
           enemies: List[organism.Organism],
           restore_player_hp: bool = True
) -> bool:
    """The battle function, the main part of the game.

    Args:
        player_object: The player which is an object of player.Player
        enemies: The enemy list for this battle.
        restore_player_hp: whether the function will restore the player's HP after the player lose the battle.

    Returns:
        A bool value represents if the player win the battle.
        True: The player win the battle.
        False: The player lose the battle.
    """
    player_origin_hp = player_object.get_property()["hp"]
    while player_object.get_property()["hp"] > 0 and enemies != []: # Keep looping until one side win.
        player_property = player_object.get_property()
        player_ad = player_property["ad"] # Player's AD for this turn.
        player_speed  = player_property["speed"] # Player's Speed for this turn.
        player_enter_correct_input = False
        while not player_enter_correct_input: # If player input invalid input, ask player input again.
            focus_aspect = input("Input which aspect the player wants to focus on: ")
            if focus_aspect == "1":
                player_ad += player_ad * .4
                player_speed -= player_speed *.3
                break
            elif focus_aspect == "2":
                player_ad -= player_ad * .4
                player_speed += player_speed *.3
                break
            else:
                print("Invalid input, Please input again.")
        
        print("Here is the enemy list, choose one as your target: ")
        enemy_number = (i+1 for i in range(len(enemies)))
        for enemy in enemies:
            print(f"{next(enemy_number)}: {enemy.get_property()['name']}")

        target_number = None
        while not player_enter_correct_input: # the user shouldn't enter number which are out of range.
            while not player_enter_correct_input:
                target_number = input("Choose one from those enemies: ")
                if target_number >= "0" and target_number <= "9":
                    break
                else:
                    print("Invalid input!")
            target_number = int(target_number)
            if target_number > 0 and target_number <= len(enemies) and target_number != None:
                break
            else:
                if len(enemies) == 1:
                    print("Invalid input, you are only allowed to enter 1.")
                else:
                    print(f"Invalid input, please enter a number from 1 to {len(enemies)}.")
        target_number -= 1 # To be a list index
        target_enemy = enemies[target_number] # Pick the target enemy.
        target_speed = target_enemy.get_property()["speed"]

        dodge_possibility = calc_dodge_possibility(
            player_speed=player_speed,
            enemy_speed=target_speed
        )

        if player_speed < target_speed:
            dodge_dice = random()
            if dodge_dice > dodge_possibility:
                enemy_hp_after_hit = enemies[target_number].get_property()["hp"] - player_ad
                enemies[target_number].change_hp(enemy_hp_after_hit)
                print(f"You hit the {target_enemy.get_property()['name']}")
            else:
                print("Miss!")
        else:
            enemy_hp_after_hit = enemies[target_number].get_property()["hp"] - player_ad
            enemies[target_number].change_hp(enemy_hp_after_hit)
            print(f"You hit the {target_enemy.get_property()['name']}")

        if enemies[target_number].get_property()["hp"] <= 0:
            print(f"The {target_enemy.get_property()['name']} is down!")
            enemies.pop(target_number)

        # Output Status
        print("Your Turn Over")
        input(f"Player HP: {player_object.get_property()['hp']}")

        for enemy in enemies:
            current_enemy_properties = enemy.get_property()
            current_enemy_speed = current_enemy_properties["speed"]
            current_enemy_ad = current_enemy_properties["ad"]
            dodge_possibility = calc_dodge_possibility(
                player_speed=player_speed,
                enemy_speed=current_enemy_speed
            )

            print(f"The {enemy.get_property()['name']} is trying to hit you!")

            if current_enemy_speed < player_speed:
                dodge_dice = random()
                if dodge_dice > dodge_possibility:
                    player_hp_after_hit = player_object.get_property()["hp"] - current_enemy_ad
                    player_object.change_hp(player_hp_after_hit)
                    print(f"You are hitted by the {enemy.get_property()['name']}")
                    print(f"Current HP: {player_object.get_property()['hp']}")
                else:
                    print("You dodged successfully!")
            else:
                player_hp_after_hit = player_object.get_property()["hp"] - current_enemy_ad
                player_object.change_hp(player_hp_after_hit)
                print(f"You are hitted by the {enemy.get_property()['name']}")
                print(f"Current HP: {player_object.get_property()['hp']}")
        
        if player_object.get_property()["hp"] <= 0:
            if restore_player_hp:
                player_object.change_hp(player_origin_hp)
            print("You lose the battle!")
            return False
        elif enemies == []:
            print("You win the battle!")
            return True
        else:
            print("Round Over.")
