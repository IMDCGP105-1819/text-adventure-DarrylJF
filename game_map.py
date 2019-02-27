import random

class MapTile:
    def __init__(self,x,y,loot):
        self.x = x
        self.y = y
        self.loot = []

    def map_location(self,x,y):
        if x < 0 or y < 0:
            return "This is impossible, try again" # coordinates can not be less than 0
        try:
            return map_of_world[y][x] # [y] selects row of map [x] selects the cell in that row
        except IndexError:
            return None # if coordinates do not exist

class StartTile(MapTile):
    def intro(self):
        return "Hi you are now in some map on a computer somewhere, be careful, there are enemies lurking" # starting room tile prints introduction text

class LootRoom(MapTile):
    def __init__(self,x,y):
        LootRoom.map_location(1,2)

class Room1(MapTile):
    def __init__(self,x,y):
        Room1.map_location(1,1)

class Room2(MapTile):
    def __init__(self,x,y):
        Room2.map_location(2,1)

class FinalRoom(MapTile):
    def __init__(self,x,y):
        FinalRoom.map_location(0,0)


        



map_of_world = [
    [FinalRoom(1,0),None,None],
    [(0,1),Room2,Room1,(3,1)],
    [None,LootRoom,(2,2),StartTile]
]