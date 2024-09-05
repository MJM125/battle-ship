
print('Welcome to Battleships for 1 player. Please be careful with entires, as if you get it wrong, you will still lose a go')
print('Good Luck')
print('')
no_of_goes = int(input("How many goes you would like?: "))
size_of_board = int(input("How big would you like the board to be?: "))
if size_of_board > 50:
    print("The board will be too big to fit on the screen (max 50)")
    size_of_board = int(input('Choose a more sensible number: '))
no_of_ships = int(input("Finally, how many ships would you like?: "))