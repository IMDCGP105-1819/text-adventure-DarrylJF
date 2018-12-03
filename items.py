import json
import enemies

class Items(object):
    def __init__(self, name, description, weight):
        self.name = name
        self.description = description
        self.weight = weight

    def __str__(self):
        return "Name: {}\n=====\nDescription: {}\nWeight: {}".format.upper(self.name, self.description, self.weight)

#inherits from base class items   
class Weapons(Items):
    def __init(self, name, description, weight, damage):
        self.damage = damage
        super().__init__(name, description, weight)
    
    def __str__(self):
        return "Name: {}\n=====\nDescription: {}\nWeight: {}\nDamage: {}".format.upper(self.name, self.description, self.weight, self.damage)

#inherits from weapons
class AK47(Weapons):
    def __init__(self):
        
        def shoot(self):
            if self.damage > 0:
                print("You can shoot")
            else:
                print("cannot shoot with this item")

class Heals(Items):
    def __init__(self, name, description, weight, value):
        self.value = value
        super().__init__(name, description, weight)

    def __str__(self):
        return "Name: {}\n=====\nDescription: {}\nWeight: {}\nValue: {}".format.upper(self.name, self.description, self.weight, self.value)


items_json = '''
{
"Weapons": [
    {
        "name": "AK-47",
        "description": "The AK-47, AK or as it is officially known as the Kalashnikov, is a gas-operated, 7.62x39mm assault rifle.",
        "weight": 0,
        "damage": 0
    }
            ],
"Heals":    [
    {
        "name": "Medic Kit",
        "description": "Will save your life",
        "weight": 0,
        "value": 0
    }
            ]
}
'''

inventory = []

items = json.loads(items_json)
#for item in items['Weapons']:
    #print(item['description'])
for item in items:
    inventory.append(Items(item["name"], item["description"], item["weight"]))
    print(inventory[0])

