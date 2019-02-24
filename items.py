"""
Items will be (classed as loot)

Weapons: Knife, Gun, Rock 

Backpack: Level 1 = 4 slots, Level 2 = 5 slots.

Level 2 backpack in first room but have to kill enemy in room 1 to 
be able to equip. However there is no weapons in room 1 so only if 
pickup rock from outside can you kill room enemy if do not pickup 
backpack will not be able to carry items in inventory.

Will give hints to pickup rock before entering first room and advise to equip a backpack.

Items will have associated actions player can invoke.

"""
from player import Player

class Items:
    def __init__(self, name, description, value, weight):
        self.name = name
        self.description = description
        self.value = value
        self.weight = weight
    
    def __str__(self):
        return f'Name: {self.name}\nDescription: {self.description}\nValue: {self.value}\nWeight: {self.weight}'

AK47 = Items("AK-47", "The AK-47, officially know as the Avtomat Kalashnikova. Automatic Rifle is a gas-operated, 7.62x39mm assault rifle", 100, 3)
SHANK = Items("Shank", "Homemade knife like weapon, especially one fashioned in prison. The related verb shiv means 'To stab someone'", 50, 1)
ROCK = Items("Rock", "Literally a rock. Pickup a rock, take no room in inventory you can keep it in ya pocket!", 100, 0)



class Backpack(object):
    def __init__(self, name, level, slots):
        self.name = name
        self.level = level
        self.slots = slots

    def __str__(self):
        return f'Name: {self.name}\nLevel: {self.level}\nSlots: {self.slots}'


BACKPACK1 = Backpack("Standard", "1", 2)


