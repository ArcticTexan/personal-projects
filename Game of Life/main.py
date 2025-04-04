import random
import time
from colorama import Fore, Back, Style

def random_state(width, height):
    board = [[0] * width for _ in range(height)]
    for row in board:
        for i in range(len(row)):
            row[i] = 1 if (random.random() >= 0.5) else 0
    return board

def render(board):
    print('_' * (2 + 3* len(board[0])))
    for row in board:
        print("|", end='', sep='')
        for cell in row:
            if (cell == 0):
                print(Fore.GREEN + ' '*3, end = "", sep = "")
            elif (cell == 1):
                print(Fore.GREEN + '█'*3, end= '', sep = '')
            else:
                print("\nERROR, Cell type unknown")
                return
        print("|")
    print('_' * (2 + 3 * len(board[0])))

def next_board(old_board):
    board = [[0] * width for _ in range(len(old_board))]
    alive_neighbors = 0
    for i in range(len(old_board)):
        for j in range(len(old_board[i])):
            alive_neighbors = 0
            alive_cell = old_board[i][j]
            alive_neighbors += old_board[ (i-1) % len(old_board)][ (j-1) % len(old_board[i])] + old_board[(i-1) % len(old_board)][j % len(old_board[i])] + old_board[(i-1) % len(old_board)][(j + 1) % len(old_board[i])] 
            alive_neighbors += old_board[i % len(old_board)][(j-1) % len(old_board[i])] + old_board[i % len(old_board)][(j+1) % len(old_board[i])]
            alive_neighbors += old_board[(i + 1) % len(old_board)][(j-1) % len(old_board[i])]+old_board[(i + 1) % len(old_board)][j % len(old_board[i])] + old_board[(i + 1) % len(old_board)][(j + 1) % len(old_board[i])]
            if alive_cell:
                if (alive_neighbors < 2 or alive_neighbors > 3):
                    board[i][j] = 0
                else:
                    board[i][j] = 1
            else:
                if (alive_neighbors == 3):
                    board[i][j] = 1
                else:
                    board[i][j] = 0
    return board
            


if __name__ == '__main__':
    dimensions = input("Enter the dimensions of your board: ")
    width, height = [int(x) for x in dimensions.split(" ")]
    board = random_state(width, height)
    # board = [[0] * width for _ in range(height)]
    # board[0][2], board[1][3], board[2][1], board[2][2], board[2][3] = 1, 1, 1, 1, 1
    print("Starting the Game of Life")
    render(board)
    while(True):
        board = next_board(board)
        render(board)
        time.sleep(.1)
