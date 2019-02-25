

"""
Game will start, player will be asked to input name and Players name will be set
via input

Player will have hp. Even though player cannot be killed, if you choose to attack 
a room enemy they will deal a blow and hp will decrease. Healable items will be in game
but if hp is <= enemy damage then you will not be able to attack unless hp > enemy
damage so you cannot die.

Player has an inventory in the form of a packpack which has 2 levels and a limited amount
of slots. Each item has a value where each 1 value represents 1 slot. i.e. Heavy valued
weapons will take up 3 slots so if you dont have enough slots you will have to drop items
before equipping.

Inventory will be a dictionary with the key being the item and an intiger for the value which
represent how many of that item is in the inventory

Player has a pocket which he can keep a single rock which he has to pick up before entering first
room so he can kill the enemy and get the level 2 backpack as there are no weapons in first room.

Once player has used rock to kill enemy the pocket will be empty and you will have the option to
pick back up.

"""

"""

Inventory
=========

Player Methods (Actions)
========================

1.) PICKUP - PICKS UP ITEM AND APPENDS IT TO INVENTORY
    
Before appending, function will check the item weight against the available backpack slots,
if enough slots are available item will be appended to inventory

2.) DROP - DROPS ITEM AND REMOVES FROM INVENTORY
   
If player drops item, value will be decremented from dict

3.) CHECK - PRINT LIST OF CURRENT INVENTORY TO CONSOLE
   
4.) HEAL - HEALS WILL INCREASE PLAYER HP BY ITS VALUE
    
Two healable items will be available each with different values
 1. Bandages - Single bandage increases hp by +10
 2. Med Kit - Puts player hp back to 100

 5.) ATTACK - ATTACKS ROOM ENEMY

 Attack checks player inventory for weapon, if weapon not present ATTACK command not available, if weapon present
 in inventory it checks room enemy hp to find best weapon
 BEST WEAPON = WEAPON DAMAGE > ENEMY HP
 
 If weapon damage !> enemy hp, player hp is checked, if player hp < enemy damage, you cannot attack, player must heal
 hp to > enemy damage to be able to attack 

 """
from items import Items
from enemies import Enemy


class Player:
    def __init__(self, name, pocket, hp, backpack):
        self.name = name
        self.pocket = {}
        self.hp = hp
        self.backpack = False

    def intro(self,name):
        return f"Hi {self.name}, heres what you can do:"

    def help_menu(self):
        f = open("help.txt", "r")

        if f.mode == "r":
            contents = f.read()
            print(contents)

    def walkthrough_file(self):
        pass

    def view_inventory(self):
        pass

    def check_health(self):
        pass

    

    




