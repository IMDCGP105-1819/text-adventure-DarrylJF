from player import Player
from rooms import Room





def main():
        game_menu = {}
        game_menu['1']="Move" # goes to player .move method "'n', 'e', 's', 'w' each going to different ingame room"
        game_menu['2']="View Inventory" # displays current inventory items
        game_menu['3']="Check Health"
        game_menu['4']="Help" # reads in .txt file for general game commands
        game_menu['5']="Game Walkthrough" # reads in .txt file for game walkthrough
        game_menu['6']="Quit"

game_on = True
while game_on:
        player_name = input("Enter your name") # get player name from input
        player = Player(player_name, {}, 100, False) # create player object
        player.intro(player_name) # player introduction text
        
        print("""
1. Move
2. View Inventory
3. Check Health
4. Help
5. Game Walkthrough
6. Quit
        """)
        
        answer=input("What do you want to do?")

        if answer == "1":
                player.move
        elif answer == "2":
                player.view_inventory()
        elif answer == "3":
                player.check_health()
        elif answer == "4":
                player.help_menu()
        elif answer == "5":
                player.walkthrough()
        elif answer == "6":
                break
        elif answer !="":
                print("Invalid entry")


if __name__ == "__main__":
   main()                 



    
