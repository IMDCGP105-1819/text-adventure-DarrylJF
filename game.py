from player import Player
from enemies import Enemy
from items import Weapon, Heals
from game_map import MapTile

"""
Game starts by asking player to enter name and saves to player_name
player character gets instantiated from player_name + health & inventory
player introduction displayed

Main game menu is displayed in a loop for the entirity of the gameplay
works in a loop so will show up after every command has finished so user can input action

"""



def main():
    player_name = input("Enter your name") # asks for user name from input
    player = Player(player_name,100,[]) # use player_name to initialise player
    player.intro() # calls Player class intro method using name input variable to greet player by name
    
    game_menu = {}
    game_menu['1']="Move" # goes to player .move method for map navigation"
    game_menu['2']="View Inventory" # displays current inventory items
    game_menu['3']="Check Health" # displays player hp
    game_menu['4']="Help" # reads in .txt file with game functionality info
    game_menu['4']="Walkthrough" # reads in .txt walkthrough file explaining how to complete game
    game_menu['5']="Quit" # end game / state not saved

    print("""
1. Move 
2. View Inventory
3. Check Health
4. Help
5. Walkthrough
6. Quit
        """)

    while True:
        room = game_map.map_location(player.x, player.y)
        print(room.intro())
        answer = player.get_player_command() # calls Player class method asking for player input
        if answer == "1":
            direc = input("What direction: ")
            if direc in ['n', 'N', 'north']:
                player.travel_north()
            elif direc in ['s', 'S', 'south']:
                player.travel_south()
            elif direc in ['e', 'E', 'east']:
                player.travel_east()
            elif direc in ['w', 'W', 'west']:
                player.travel_west()
        elif answer == "2":
            player.view_inventory()
        elif answer == "3":
            player.hp()
        elif answer == "4":
            player.view_help_file()
        elif answer == "5":
            player.view_walkthrough_file()
        elif answer == "6":
            print("Ok no dramas")
            break
        elif answer != "":
            print("Invalid entry")
            
if __name__ == "__main__":
    main()


