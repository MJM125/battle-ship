from random import randint
print('Welcome to Battleships for 1 player. Please be careful with entires, as if you get it wrong, you will still lose a go')
print('Good Luck')
print('')
no_of_goes = int(input("How many goes you would like?: "))
size_of_board = int(input("How big would you like the board to be?: "))
if size_of_board > 50:
    print("The board will be too big to fit on the screen (max 50)")
    size_of_board = int(input('Choose a more sensible number: '))
no_of_ships = int(input("Finally, how many ships would you like?: "))
board = []

for x in range(size_of_board):
    board.append(["O"] * size_of_board)

def print_board(board):
    for row in board:
        print ("  ".join(row))
print_board(board)
ship_rows = []
ship_cols = []

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board) - 1)
ships = list(range(no_of_ships))
for i in ships:
    row = random_row(board)
    col = random_col(board)
    ship_rows.append(row)
    ship_cols.append(col)

    for row in ship_cols:
        if row == ship_cols and col == ship_cols:
            ship_rows[-1] = random_row(board)
            ship_cols[-1] = random_col(board)
print(ship_rows)
print(ship_cols)
ship_count = [1]

def printing_stars():
    print('You have won! ' +'*' * 50)
    printing_stars()
for turn in range(no_of_goes):
    print('Turn ' + str(turn + 1) + ' out of ' + str(no_of_goes))
    guess_col = int(input("Guess Column: ")) - 1
    guess_row = int(input("Guess Row: ")) - 1
    for item in ship_rows:
        if len(ship_count) == no_of_ships and guess_row == item and guess_col == ship_cols[ship_rows.index(item)]:
            print("Congratulations! You have won!")
            board [guess_row][guess_col] = '!'
            print_board(board)
            printing_stars()

        elif guess_row == item and guess_col == ship_cols[ship_rows.index(item)]:
            print ("Congratulations! You've sunk my battleship")
            board [guess_row][guess_col] = '!'
            print_board(board)
            ship_count.append[1]
            break
    else:
        if (guess_row < 0 or guess_row > size_of_board - 1) or (guess_col < 0 or guess_col > size_of_board - 1):
            print("Aim for water not land")

        elif board[guess_row][guess_col] == "X" or board[guess_row][guess_col] == "!":
            print("You can only fire at a spot once, try again")
            turn =- 1
        
        else:
            print("Missile overboard, try again")
            board[guess_row][guess_col] = "X"
        print_board(board)
        if turn == (no_of_goes - 1):
            print("Game Over, better luck next time")
            break