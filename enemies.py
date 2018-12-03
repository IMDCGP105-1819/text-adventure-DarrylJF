class Enemies(object):
    def __init__(self, name, description, hp, damage):
        self.name = name
        self.description = description
        self.hp = hp
        self.damage = damage
    
class Squatter(Enemies):
    def __init__(self):
        pass