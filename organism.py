"""This file describe the base class of all the living things in this game.
"""

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
