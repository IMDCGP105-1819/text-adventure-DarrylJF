
"""
Enemies will have hp value which will be attached to a player attack function where it the game
will suggest best weapon of attack based on enemy hp and weapon damage if player has in there
inventory. 

If weapons in inventory dont have value game will tell you unable to kill with current
arsenal and suggest next best weapon.

If you have to use two attacks to kill enemy player will have to take a blow and player hp will be
checked and if hp < enemy attack value you will not be able to attack unless you heal to a > hp first

"""
from player import Player

class Enemy:
    def __init__(self, name, description, hp, damage):
        self.name = name
        self.description = ""
        self.hp = hp
        self.damage = damage
