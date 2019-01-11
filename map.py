from .tiles import MapTile

_map = {}
starting_position = (0,0)

def load_Tiles():
    """Parses file to give visual of layout"""
    with open("text_adventure_main/map.txt", "r") as f:
        rows = f.readlines()
    x_max = len(rows[0].split("\t"))
    for y in range(len(rows)):
        cols = rows[y].split('\t')
        for x in range(x_max):
            tile_name == cols[x].replace('\r', '')
            if tile_name == "Room1":
                global starting_position
                starting_position = (x,y)
            _map[(x,y)] = None if tile_name == '' else getattr(__import__('tiles'), tile_name)(x,y) 

""" trying to parse txt file and iterate through each line and split the line into individual cells
double for loop is apparently a common way to do this. x and y are the coordinated and we set the starting 
coordinates to Room1.

the _map is a dictionary that should map a coordinate pair to the file so the code _map[(x,y)] if the coordinate pair
is an empty string we dont store a tile in its place. 

ti"""