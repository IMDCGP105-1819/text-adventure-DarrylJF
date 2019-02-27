class Enemy:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def __str__(self):
        return f"\nName: {self.name}\nHP: {self.hp}\nAttack: {self.attack}"

    def dead_or_alive(self):
        return self.hp > 0

class LootRoomSquatter(Enemy):
    def __init__(self):
        self.name = "Squatter"
        self.hp = 100
        self.attack = 0

class Room1Enemy(Enemy):
    def __init__(self):
        self.name = "Ninja"
        self.hp = 1000 
        self.attack = 50

class Room2Enemy(Enemy):
    def __init__(self):
        self.name = "John has a gun, but hes slow"
        self.hp = 100
        self.attack = 50



    

        