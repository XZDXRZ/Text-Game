"""This file define the enemy, Thief.
"""

import organism

THIEF_AD = 30
THIEF_SPEED = 35
THIEF_HP = 80

class Thief(organism.Organism):
    """This class define the thief.

    Attributes:
        ad: Attack Damage.
        speed: A Varible which decide the possibility of the thief can avoid an attack.
        hp: Health Point.
        name: Name for output.
    """
    def __init__(self):
        super().__init__(THIEF_AD, THIEF_SPEED, THIEF_HP, "Thief")
        self.ad = THIEF_AD
        self.speed = THIEF_SPEED
        self.hp = THIEF_HP
        self.name = "Thief"
