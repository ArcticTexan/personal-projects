import random
import time
import itertools

def initializeBoard():
    return [[" "]*3 for _ in range(3)] # Returns 3 by 3 grid

def renderGrid(board):
    output = " 0 1 2 \n  ______\n"
    for i in range(len(board)):
        output += str(i) + '|'
        for cell in board[i]:
            output += cell + ' '
        output = output[:-1]
        output += '|\n'
    output += "  ______"
    print(output)

def updateBoard(board, x, y, player = 'X', silent = False):
    new_board = initializeBoard()
    for i in range(3):
        for j in range(3):
            new_board[i][j] = board[i][j]
    if new_board[x][y] == ' ':
        new_board[x][y] = player
    else:
        raise Exception("This spot is occupied")
    return new_board

def checkForWin(board):
    hasEmpty = False
    for i in range(3):
        if board[i][0] != ' ':
            if (board[i][0] == board[i][1] and board[i][0] == board [i][2]):
                return board[i][0]
        if board[0][i] != ' ':
            if (board[0][i] == board[1][i] and board[1][i] == board[2][i]):
                return board[0][i]
        if board[1][1] != ' ':
            if (board[1][1] == board[0][0] and board [1][1] == board [2][2]):
                return board[1][1]
            if (board[1][1] == board[0][2] and board [1][1] == board [2][0]):
                return board[1][1]
        for j in range(3):
            if board[i][j] == ' ':
                hasEmpty = True
    if hasEmpty == False:
        return 'D'
    else: return ' '
    

def randomLegalMove(board, player = 'X'):
    legal_moves = []
    for i in range(3):
        for j in range(3):
            if not isNotLegal(board,i,j):
                legal_moves.append(i,j)
    random.shuffle(legal_moves)
    return legal_moves[0]
        
def isNotLegal(board, x, y):
    if x not in [0,1,2] or y not in [0,1,2]:
        return True
    if board[x][y] != ' ':
        return True
    return False
        
def playsWinningMove(board, player = 'X'):
    legal_moves = []
    for i in range(3):
        for j in range(3):
            if not isNotLegal(board,i,j):
                legal_moves.append(i,j)
    for move in legal_moves:
        newboard = updateBoard(board,move[0],move[1], player)
        if(checkForWin(newboard) != ' '):
            return move                
    random.shuffle(legal_moves)
    return legal_moves[0]

def minmax(board, player):
    if (checkForWin(board) != ' '):
        if checkForWin(board) == 'D':
            return 0
        elif checkForWin(board) == 'X':
            return 10
        else:
            return -10
    movedict = dict()
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                movedict[(i,j)] = -99
    for move in movedict:
        newboard = updateBoard(board,move[0],move[1], player)
        if (player == 'X'):
            movedict[move] = minmax(newboard,'O')
        elif (player == 'O'):
            movedict[move] = minmax(newboard, 'X')
    if (player == 'O'):
        candidate = min(movedict, key=movedict.get)
    elif (player == 'X'):
        candidate = max(movedict, key=movedict.get)
    return movedict[candidate]
   
def minmax_ai(board, player = 'X'):
    legal_moves = []
    cscore = None
    candidate = None
    playercopy = player
    for i in range(3):
        for j in range(3):
            if not isNotLegal(board,i,j):
                legal_moves.append([i,j])
    movedict = dict()
    for pmove in legal_moves:
        newboard = updateBoard(board,pmove[0],pmove[1], playercopy)
        if (player == 'X'):
            nextPlayer = 'O'
        elif (player == 'O'):
            nextPlayer = 'X'
        cscore = minmax(newboard,nextPlayer)
        movedict[(pmove[0],pmove[1])] = cscore
    if (player == 'O'):
        candidate = min(movedict, key=movedict.get)
    elif (player == 'X'):
        candidate = max(movedict, key=movedict.get)
    return candidate

if __name__ == '__main__':
    print("Welcome to Tic-Tac-Toe!")
    playerNum = int(input("How many players? "))
    if (playerNum == 1):
        # playAI()
        print("Starting game against AI")
        board = initializeBoard()
        renderGrid(board)
        player = 'X'
        while(checkForWin(board) == " "):
            if (player == 'X'):
                x = int(input("Enter the X coordinate for your move: "))
                y = int(input("Enter the Y coordinate for your move: "))
                while(isNotLegal(board, x,y)):
                    print("Not a valid location, try again")
                    x = int(input("Enter the X coordinate for your move: "))
                    y = int(input("Enter the Y coordinate for your move: "))
            else:
                x, y = minmax_ai(board, player)
            board = updateBoard(board, x, y, player)
            renderGrid(board)
            player = 'O' if player == 'X' else 'X'
        if checkForWin(board) == 'D':
            print("It's a draw, better luck next time!")
        elif checkForWin(board) == 'X':
            print("Player 1 wins! Good Job!")
        else:
            print("Player 2 wins! Good Job!")

    elif (playerNum == 2):
        # play2p()
        print("Starting game against another player")
        board = initializeBoard()
        renderGrid(board)
        player = 'X'
        while(checkForWin(board) == " "):
            x = int(input("Enter the X coordinate for your move: "))
            y = int(input("Enter the Y coordinate for your move: "))
            while(isNotLegal(board, x,y)):
                print("Not a valid location, try again")
                x = int(input("Enter the X coordinate for your move: "))
                y = int(input("Enter the Y coordinate for your move: "))
            board = updateBoard(board, x, y, player)
            renderGrid(board)
            player = 'O' if player == 'X' else 'X'
        if checkForWin(board) == 'D':
            print("It's a draw, better luck next time!")
        elif checkForWin(board) == 'X':
            print("Player 1 wins! Good Job!")
        else:
            print("Player 2 wins! Good Job!")
            
        
    elif (playerNum == 0):
        print("Starting CPU game")
        board = initializeBoard()
        renderGrid(board)
        player = 'X'
        while(checkForWin(board) == " "):
            print("Minmax eval is: ", minmax(board,player))
            x, y = minmax_ai(board, player)
            board = updateBoard(board, x, y, player)
            renderGrid(board)
            player = 'O' if player == 'X' else 'X'
        if checkForWin(board) == 'D':
            print("It's a draw, better luck next time!")
        elif checkForWin(board) == 'X':
            print("Player 1 wins! Good Job!")
        else:
            print("Player 2 wins! Good Job!")

    elif (playerNum == -1):
        legalMoves = []
        player = 'O'
        board = [['X', 'O', ' '],[' ','O',' '],[' ','X',' ']]
        for i in range(3):
                for j in range(3):
                    if board[i][j] == ' ':
                        legalMoves.append([i,j])
        for move in legalMoves:
            tempBoard = updateBoard(board, move[0], move[1], 'O')
            renderGrid(tempBoard)
            print(minmax(tempBoard,'X'))
            
    else:
        print("Only 0-2 players can play")
        