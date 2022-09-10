"""This file describe the class Player which represents player.
"""

import organism

PLAYER_AD = 0
PLAYER_SPEED = 30
PLAYER_HP = 100

class Player(organism.Organism):
    """Define the player and its properties.

    Attributes:
        ad: Attack Damage.
        speed: A variable for dodge.
        hp: health point.
        name: Player's name which the player entered in the beginning.
    """
    def __init__(self):
        super().__init__(PLAYER_AD, PLAYER_SPEED, PLAYER_HP, "Player")
        self.ad = PLAYER_AD
        self.speed = PLAYER_SPEED
        self.hp = PLAYER_HP
        self.name = "Player"

    def change_property(self,
                        ad: int,
                        speed: int,
                        hp: int,):
        """Change the properties such as AD, Speed and HP for this player.
        """
        self.ad = ad
        self.speed = speed
        self.hp = hp

    def change_name(self,
                    name: str):
        """Change the name of player.
        """
        self.name = name
