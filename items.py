import json

class Items(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return "Name: {}\n=====\nDescription: {}\n".format.upper(self.name, self.description)

#inherits from base class items   
class Weapons(Items):
    def __init(self, damage, weight):
        self.damage = damage
        self.weight = weight

    def __str__(self):
        return "Name: {}\n=====\nDescription: {}\nDamage: {}\nWeight: {}".format.upper(self.name, self.description, self.damage, self.weight)

#inherits from weapons
class AK47(Weapons):
    def __init__(self):
        
        def shoot(self):
            if self.damage > 0:
                print("bang bang")
            else:
                print("cannot shoot with this item")

class Heals(Items):
    def __init__(self):
        pass





        

items_json = json

items = json.loads(items_json)

inventory = []

for item in items:
    inventory.append(Items(item["name"], item["description"], item["level"], item["damage"]))

