import numpy as np
game_board = np.zeros(shape=(3, 3))


# Creating a view, but using a slice, so we can address
# only a portion of the elements.
game_board = np.arange(1, 10).reshape(3, 3)

row0 = game_board[0]
row1 = game_board[1]
row2 = game_board[2]

column1 = game_board[:, 0]
column2 = game_board[:, 1]
column3 = game_board[:, 2]

# Using numpy.eimsum to create diagnonals
diag0 = np.einsum('ii->i', game_board)
diag1 = np.einsum('ii->i', np.fliplr(game_board))

diag0[:] = 1
diag1[2] = 9

def check_win_state(tile):
    tile = ord(tile)
    print(row0)
    # if row0 = tile or row1 = tile or row2 == tile:
    #     print("The winner is " + str(tile))

def make_move(x_cord, y_cord, tile):
    # convcert tile to ASCII value
    tile = ord(tile)
    game_board[x_cord][y_cord] = tile


make_move(0, 0, 'X')
make_move(1, 0, 'X')
make_move(2, 0, 'X')

check_win_state('X')
print(game_board)
