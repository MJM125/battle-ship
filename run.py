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