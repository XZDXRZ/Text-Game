"""This File describe the enemies, Slime in this game.
This file contains Slime, inherit from base class Enemy.
"""

import organism

SLIME_AD = 10
SLIME_SPEED = 30
SLIME_HP = 60

class Slime(organism.Organism):
   """This describe the enemy, Slime in this game.

   Attributes:
        ad: Attack Damage of the organism.
        speed: A Varible which decide the possibility of the organism can avoid an attack.
        hp: Health Point of the organism.
        name: "Slime" for output
   """
   def __init__(self):
      super().__init__(SLIME_AD, SLIME_SPEED, SLIME_HP, "Slime")
      self.ad = SLIME_AD
      self.speed = SLIME_SPEED
      self.hp = SLIME_HP
      self.name = "Slime"
