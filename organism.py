"""This file define the base class of all the living things in this game.
"""

from typing import Dict

class Organism(object):
    """This is the base class of all the living things in this game.

    Attributes:
        ad: Attack Damage of the organism.
        speed: A Varible which decide the possibility of the organism can avoid an attack.
        hp: Health Point of the organism.
        name: The Object's name such as Slime
    """
    def __init__(self,
                 ad: int,
                 speed: int,
                 hp: int,
                 name: str):
        self.ad = ad
        self.speed = speed
        self.hp = hp
        self.name = name

    def get_property(self) -> Dict[str, int or str]:
        """Get a organism's property: AD, Speed, HP, Name

        Returns:
            Dict: A dictionary contains all the properties of an organism.
        """
        properties = {
            "ad" : self.ad,
            "speed" : self.speed,
            "hp" : self.hp,
            "name" : self.name
        }
        return properties

    def change_hp(self,
                  hp: int):
        """Change an object's HP.
        """
        self.hp = hp
