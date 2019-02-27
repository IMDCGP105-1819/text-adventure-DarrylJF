class Weapon:
    def __init__(self, name, description, weight, damage):
        self.name = name
        self.description = description
        self.weight = weight
        self.damage = damage
    
    def __str__(self):
        return f"\nName: {self.name}\nDescription: {self.description}\nWeight: {self.weight}\nDamage: {self.damage}"

class Knife(Weapon):
    def __init__(self):
        self.name = "Knife"
        self.description = "Shank, effective close range"
        self.weight = 1
        self.damage = 50

class AK47(Weapon):
    def __init__(self):
        self.name = "AK-47"
        self.description = "Also known as the Kalashnikov"
        self.weight = 2
        self.damage = 100

class Rock(Weapon):
    def __init__(self):
        self.name = "Rock"
        self.description = "By any means necessary"
        self.weight = 0
        self.damage = 25

class Heals:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value
    
    def __str__(self):
        return f"\nName: {self.name}\nWeight: {self.weight}\nHeal Value: {self.value}"

class Bread(Heals):
    def __init__(self):
        self.name = "Bread"
        self.weight = 0
        self.value = 10

class Bandage(Heals):
    def __init(self):
        self.name = "Bandage"
        self.weight = 0
        self.value = 25

class MedKit(Heals):
    def __init__(self):
        self.name = "Med Kit"
        self.weight = 1
        self.value = 100








