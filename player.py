from .items import Item

class Player(object):
    def __init__(self):
        self.inventory = [Item.shank()]
        self.hp = 100
        self.location_x, self.location_y = map.starting_position

    def is_Alive(self):
        return self.hp > 0

    def check_Inventory(self):
        for item in self.inventory:
            print(item, '\n')

    def move(self,dx,dy):
        self.location_x +=dx
        self.location_y +=dy
        print(map.tile_exists(self.location_x, self.location_y).intro_text())

    def move_North(self):
        self.move(dx=0,dy=-1)

    def move_South(self):
        self.move(dx=0,dy=1)

    def move_East(self):
        self.move(dx=1,dy=0)

    def move_West(self):
        self.move(dx=-1,dy=0)

