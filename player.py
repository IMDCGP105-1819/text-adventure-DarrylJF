from items import Weapon
from items import Heals

class Player:
    def __init__(self, name, hp, inventory):
        self.name = name
        self.hp = hp
        self.inventory = [Weapon.Rock(),
                          Heals.bandage()]
        self.x = 1
        self.y = 2

    def intro(self):
        return f"Hi {self.name}, welcome to the game"

    def get_player_command(self):
        return input("What do you want to do: ")

    def view_inventory(self):
        for item in self.inventory:
            print("\nInventory: " + item)

    def view_help_file(self):
        f = open("help.txt" "r")
        if f.mode == "r":
            contents = f.read()
            print(contents)

    def view_walkthrough_file(self):
        f = open("walkthrough.txt", "r")
        if f.mode == "r":
            contents = f.read()
            print(contents)
    
    def view_health(self):
        return self.hp

    def heal(self):
        healeables = [item for item in self.inventory if isinstance(item,items.Heals)]  

    def find_best_weapon(self,inventory): # goes into player inventory and compares each item.damage and returns weapon with highest damage
        max_dmg = 0
        best_weap = None # if player does not have weapon 
        for item in inventory:
            try:
                if item.damage > max_dmg:
                    best_weap = item
                    max_dmg = item.damage
                    print(f"\n{best_weap} is your best weapon with a damage of {max_dmg}")
            except AttributeError: # exception if no weapon with .damage attribute exist in inventory, i.e. med kit will have no damage attribute
                pass

            return best_weap
        

    # PLAYER MOVE
    def travel(self, movex, movey):
        self.x += movex
        self.y += movey

    def travel_north(self):
        self.travel(movex=0, movey=-1)
    
    def travel_south(self):
        self.travel(movex=0,movey=1)

    def travel_east(self):
        self.travel(movex=1, movey=0)

    def travel_west(self):
        self.travel(movex=-1,movey=0)