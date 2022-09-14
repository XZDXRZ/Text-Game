"""This Python File define some functions for presenting the story.
"""

import player
import battle
import print_help_doc
import slime
import thief

player_name = None
player_object = player.Player()

def play_chapter0():
    """This part describe the Prologue.
    """

    print("==================")
    print("|    Prologue    |")
    input("==================")

    player_enter_correct_input = False
    while not player_enter_correct_input: # Player enter the name
        player_name = input("Please enter your name to start the game: ")
        if player_name != "":
            break
        else:
            input("Please enter something.")
    player_object.change_name(player_name)

    input(player_object.get_name() + " wake up from bed and heading towards school, but a truck hits him.")
    input("After a while of unconscious.")
    input("You wake up and found you have gone to another world.")
    input("You look around and find yourself are sitting on the bed in an old wooden house.")
    input("There is some weapons on the table beside you, pick one to get armed.")

    while not player_enter_correct_input:
        player_property = player_object.get_property()
        weapon_player_chosen = input("Please enter 1 or 2.\n1 refers to sword and heavy armor. And 2 refers to bow and light armor: ")
        if weapon_player_chosen == "1":
            player_object.change_property(
                player_property["ad"] + 120, # AD
                player_property["speed"] - 10,  # Speed
                player_property["hp"] + 150  # HP
            )
            break
        elif weapon_player_chosen == "2":
            player_object.change_property(
                player_property["ad"] + 70, # AD
                player_property["speed"] + 20,  # Speed
                player_property["hp"] + 70  # HP
            )
            break
        else:
            input("Invalid input, please enter 1 or 2.")
    
    input("As you open up the door, a slime appears.")
    input("Battle starts, the enemy is a Slime.")

    print_help_doc.print_battle_help() # This is the first battle, so print the tutorial.
    player_lose_the_battle = True
    while player_lose_the_battle:
        player_lose_the_battle = not battle.battle(
            player_object=player_object,
            enemies=[
                slime.Slime()
            ]
        ) # Whether the player win the game.
        if player_lose_the_battle:
            input("How could you lose? Anyway, you have gained another life, do it again.")
    
    input("You find youself are in a village which is attacking by slimes. You can see the village chief is walking towards you.")
    input("From the words of the village chief, you get to know that the village is attacked frequently recently, and he wants you to investigate the reason.")
    input("You accept the commission and start on your journey.")

    print("===================")
    print("| End of Prologue |")
    input("===================")

def play_chapter1():
    """Chapter 1.
    """
    
    print("===================")
    print("|    Chapter 1    |")
    input("===================")

    input("You are walking around the village, you found some slime are heading towards the village. You decide to wipe out them.")

    input(f"Battle between {player_object.get_name()} and three slimes starts!")
    player_lose_the_battle = True
    while player_lose_the_battle:
        player_lose_the_battle = not battle.battle(
            player_object=player_object,
            enemies=[
                slime.Slime(),
                slime.Slime(),
                slime.Slime()
            ]
        )
        if player_lose_the_battle:
            input("How could you lose? Anyway, you have gained another life, do it again.")

    input("After the battle, you find a piece of paper on the ground. That's a map to an unknow place.")
    input("As you focusing on the map, a strange man appears from  the grass. Suddenly, he attacked you!")

    input(f"Battle between {player_object.get_name()} and a strange man starts!")
    player_lose_the_battle = True
    while player_lose_the_battle:
        player_lose_the_battle = not battle.battle(
            player_object=player_object,
            enemies = [
                thief.Thief()
            ]
        )
        if player_lose_the_battle:
            input("How could you lose? Anyway, you have gained another life, do it again.")
    
    input("You realized that the map is not as safe as you thought.")
    input("You follow the direction of the map and come to a cave.")
    input("You find two strange men and some slimes in the cave.")
    input("The two men are discussing something. You hear from them that they are training the slimes to attack the village due to some reasons.")
    input("You are angry about this, and decide to give them a lesson.")

    input("Battle starts, the enemies are 2 strange men and 1 slime.")
    player_lose_the_battle = True
    while player_lose_the_battle:
        player_lose_the_battle = not battle.battle(
            player_object=player_object,
            enemies = [
                thief.Thief(),
                thief.Thief(),
                slime.Slime(),
            ]
        )
        if player_lose_the_battle:
            input("Don't be sad, do it again.")
    
    input("As you finishing battle, some other slimes realize you are here and start attacking you.")
    
    input("Battle starts, the enemies are 3 slimes.")
    player_lose_the_battle = True
    while player_lose_the_battle:
        player_lose_the_battle = not battle.battle(
            player_object=player_object,
            enemies = [
                slime.Slime(),
                slime.Slime(),
                slime.Slime(),
            ]
        )
        if player_lose_the_battle:
            input("How could you lose? Anyway, you have gained another life, do it again.")
    
    input("You find their plan on a table.")
    input("They are being leaded by a organization which is hostile to this country.")
    input("You know, your journey is still long...")
    input("To be continued...")

    print("====================")
    print("| End of Chapter 1 |")
    input("====================")

if __name__ == "__main__":
    play_chapter1() # Debug
