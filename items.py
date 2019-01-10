class Item(object):
    def __init__(self, name, description, weight):
        self.name = name 
        self.description = description
        self.weight = weight

    def __str__(self):
        return f"\nName: {self.name}\nDescription: {self.description}\nWeight: {self.weight}"

# backpacks have spaces and all other items will have a 'weight' which will be an integer
# two levels of backpacks level 1 with 4 slots and level 2 with 5 slots
# if player reaches max slots will have to drop item first

class backpack(Item):
    def __init__(self, level, spaces):
        self.level = level
        self.spaces = spaces 
        super().__init__(name="Backpack", # call to superclass constructor to initialise additional parameters
                         description=f"This backack is level {self.level}. It has {self.spaces} spaces for items you find",
                         level=self.level,
                         spaces=self.spaces)
    
    def __str__(self):
        return f"\nName: {self.name}\nDescription: {self.description}"


class Weapon(Item):
    def __init__(self,name,description,weight,damage):
        self.damage = damage
        super().__init__(name,description,weight)

    def __str__(self):
        return f"\nName: {self.name}\nDescription: {self.description}\nWeight: {self.weight}\nDamage: {self.damage}"


class Ak47(Weapon):
    def __init__(self):
        super().__init__(name="AK-47",
                         description="The AK-47, officially known as the Avtomat Kalashnikov",
                         weight=3,
                         damage=100)

class Shank(Weapon):
    def __init__(self):
         super().__init__(name="Shank",
                         description="Improvised prison melee weapon to take down enemies in close quarters and steal their dogtags.",
                         weight=1,
                         damage=25)

