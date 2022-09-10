"""This Python File describe a function for presenting the story.
"""

import player
import battle
import print_help_doc
import slime

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
            print("Please enter something.")
    player_object.change_name(player_name)

    input(player_object.name + " wake up from bed and heading towards school, but a truck hits him.")
    input("After a while of unconscious.")
    input("You wake up and found you have gone to another world.")
    input("You look around and find yourself are sitting on the bed in an old wooden house.")
    input("There is some weapons on the table beside you, pick one to get armed.")

    while not player_enter_correct_input:
        weapon_player_chosen = input("Please enter 1 or 2.\n1 refers to sword and heavy armor. And 2 refers to bow and light armor: ")
        if weapon_player_chosen == "1":
            player_object.change_property(
                player_object.ad+120,
                player_object.speed-10,
                player_object.hp+150
            )
            break
        elif weapon_player_chosen == "2":
            player_object.change_property(
                player_object.ad+70,
                player_object.speed+20,
                player_object.hp+70
            )
            break
        else:
            print("Invalid input, please enter 1 or 2.")
    
    input("As you open up the door, a slime appears.")
    print("Battle start, the enemy is Slime.")

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
            print("How could you lose? Anyway, you have gained another life, do it again.")
    
    print("You find youself are in a village which is attacking by slimes. You can see the village chief is walking towards you.")
    print("From the words of the village chief, you get to know that the village is attacked frequently recently, and he wants you to investigate the reason.")
    input("You accept the commission and start on your journey.")

    print("===================")
    print("| End of Prologue |")
    input("===================")
