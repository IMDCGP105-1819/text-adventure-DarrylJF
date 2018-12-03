import json
import items

items_json = json

items = json.loads(items_json)

inventory = []

class Player(object):
    def __init__(self, inventory, hp, victory):
        self.inventory = []
        self.hp = 100
        self.victory = False
    
    # used for game loop to check if game is over 
    def is_alive(self):
        return self.hp > 0

    # prints whatever is currently in players inventory
    def print_inventory(self):
        for item in self.inventory:
            if len(inventory) == 0:
                print("There is currently no items in your inventory")
            else:
                print(item, '\n')

    # attack method, 
    def attack(self, enemies):
        best_weapon = None
        max_dmg = 0
        for i in self.inventory:
            if isinstance(i, items.Weapon):
                if i.damage > max_dmg:
                    max_dmg = i.damage
                    best_weapon = i

    def pickup(self, items):

        pass

        