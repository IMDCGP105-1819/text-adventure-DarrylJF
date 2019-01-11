from .items import Item
from .enemies import Enemy

class MapTile(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

def intro_text(self):
    raise NotImplementedError()

def modify_player(self):
    raise NotImplementedError()


class Room1(MapTile):
    def intro_Text(self):
        return """
        some text to describe the layout of room
               """
    
    def modify_Player(self,player):
        pass

class Room_With_Loot(MapTile):
    def __init__(self,x,y,item):
        self.item = item
        super().__init__(x,y)

    def add_Loot(self,player):
        player.inventory.append(self.item)

    def modify_Player(self,player):
        self.add_Loot(player)

class Room_With_Enemy(MapTile):
    def __init__(self,x,y,enemy):
        self.enemy = enemy
        super().__init__(x,y)

    def gun_Selection(self, a_player):
        pass 

    def modify_Player(self,x,y,a_player):
        if self.enemy.is_alive():
            a_player.hp = a_player.h - self.enemy.damage
            print(f"{self.enemy.damage}{a_player.hp}")

class enemy_2_Room(Room_With_Enemy):
    def __init__(self,x,y):
        super().__init__(x,y,Enemy.room_2_enemy())

    def room_Description(self):
        return ""

class find_Ak47_Room(Room_With_Loot):
    def __init__(self,x,y):
        super().__init__(x,y,Item.Ak47())

class find_Backpack_Room(Room_With_Loot):
    def __init__(self,x,y):
        super().__init__(x,y,Item.Backpack())

    def room_Description(self):
        return ""


    

    