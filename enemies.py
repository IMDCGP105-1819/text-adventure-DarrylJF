import json

class Enemies(object):
    def __init__(self, name, description, hp, damage):
        self.name = name
        self.description = description
        self.hp = hp
        self.damage = damage

    def __str__(self):
        return "Name: {}\n=====\nDescription: {}\nHP: {}\nDamage: {}".format.upper(self.name, self.description, self.hp, self.damage)
    
class Squatter(Enemies):
    def __init__(self, name, descrition, hp, damage):
        pass