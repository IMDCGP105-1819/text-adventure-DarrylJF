# player enters room and is presented with a list of actions available to them
# each room will have an enemy. player can not die but can use loot items to attack enemies
# each room will have loot items which you can add to player inventory
# each room will have a storyline
# you can only visit rooms once. visited attribute set to False by default and will be set to True once player leaves room. once all rooms have been visited game is over.
class Room:
    def __init__(self, name, loot, enemy, story, visited):
            self.name = name
            self.loot = ()
            self.enemy = enemy
            self.story = ()
            self.visited = False


