"""
    Battleships!
    
Classes to create:
    Main
    Ship
    Board
    

"""
from board_battle_ships import Board
#from ships_battle_ships import Ship
from random import randint

board_main = Board(1, 1) #initilize board

board_main.create_board() #set board size and print board

#choosing number of ships, with limits
count = 0
num_ships = input("Choose between 1 and 5 ships:")
num_ships = int(num_ships)
if num_ships > 5 or num_ships < 1:
    while (num_ships > 5 or num_ships < 1) and count <= 10:
        print("Please chose between 1 and 5, and try again")
        num_ships = input("Choose between 1 and 5 ships:")
        num_ships = int(num_ships)
        count += 1
    if count >= 10:
        print("Game over, listen or go home")
    else:
        print ("You chose %s ships! Randomly placing them now" % (num_ships))
else:
    print ("You chose %s ships! Randomly placing them now" % (num_ships))

#creating ships
ship_list = []
for i in range(1, board_main.num_x + 1):
            ship_list.append(["O"] * int(board_main.num_y))
for i in range(0, num_ships):
    ship_list[randint(1,board_main.num_x - 1)][randint(1,board_main.num_y) - 1] = "X"

for i in ship_list:
    print (i)
    
#take guesses
count1 = 0
while count1 < num_ships:
    count = 0
    if count < 15:
        y = input("Take a guess at y position: ")
        x = input("Take a guess at x position: ")
        x = int(x) - 1
        y = int(y) - 1
        if ship_list[y][x] == "X":
            print("You have sunk my ship!")
            board_main[y][x] = "!"
            count1 += 1
            board_main.print_board()
        else:
            print("You have missed my ship!")
            board_main[y][x] = "X"
            count += 1
            board_main.print_board()
    else:
        print("You have run out guesses! Game Over!!")





#print("The position of my ship was; x --> %s and y--> %s" % (ship.x_pos, ship.y_pos))
 

