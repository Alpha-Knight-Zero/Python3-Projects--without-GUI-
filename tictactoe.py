import random

usrSign=0
aiSign=1
signs=["X","O"]
user=""
board=[" " for x in range(9)]

print("Welcome to this game of Tic-Tac-Toe !!!")
user=input("Enter the username : ")
print(user,", enter 0 to play as X or 1 to play as 0 :")
usrSign=int(input())
aiSign-=usrSign
usrSign=signs[usrSign]
aiSign=signs[aiSign]

def makeMove(sign,pos):
    global board
    board[pos]=sign

def checkIfFree(pos):
    return board[pos]==" " 

def printBoard():
    for i in range(3):
        print("\t ",board[i*3]+" | "+board[i*3+1]+" | "+board[i*3+2])
        if i!=2 :
            print("\t","-"*11)

def isBoardFull():
    global board
    return board.count(" ")==0

def checkWinner(board,sign):
    for i in range(3):
        if board[i*3]==sign and board[i*3+1]==sign and board[i*3+2]==sign:
            return 1
        elif board[i]==sign and board[i+3]==sign and board[i+6]==sign:
            return 1
    for i in range(0,3,2):
        if board[i]==sign and board[4]==sign and board[8-i]==sign:
            return 1
    return 0

def playerMove():
    while True:
        print("Please enter the place to mark with",usrSign,"(from 1 to 9 , positions are arranged rowise) :",end=" ")
        move=input()
        try:
            move=int(move)-1
            if move in range(0,9):
                if checkIfFree(move):
                    makeMove(usrSign,move)
                    break
                else:
                    print("Sorry , that position is already occupied. Enter an empty position to mark.")
                    printBoard()
            else :
                print("Sorry , wrong position entered , please enter a position from 1 to 9.")

        except:
            print("Sorry wrong type of input given, please enter an integer.")

def aiMove():
    possibleMoves=[x for x, letter in enumerate(board) if letter==" "]
    for letter in signs:
        for i in possibleMoves:
            boardcpoy=board[:]
            boardcpoy[i]=letter
            if checkWinner(boardcpoy,letter):
                return i
    move=-1
    
    cornersOpen=[]
    for i in possibleMoves:
        if i in [0,2,6,8]:
            cornersOpen.append(i)
    if len(cornersOpen):
        move=selectRandom(cornersOpen)
        return move
    
    if 5 in possibleMoves:
        move=5
        return move
    
    restOpen=[]
    for i in possibleMoves:
        if i in [1,3,5,7]:
            restOpen.append(i)
    if len(restOpen):
        move=selectRandom(restOpen)
        return move

def selectRandom(list):
    return random.randint(0,len(list))

def game():
    printBoard()
    global board
    while not isBoardFull():
        if not checkWinner(board,aiSign):
            playerMove()
            printBoard()
        else :
            print("You lose. Better luck next time.")
            break
        
        if not checkWinner(board,usrSign):
            if isBoardFull():
                print("The game has ended in a tie.")
            else :
                move=aiMove()
                makeMove(aiSign,move)
                print("Computer has placed",aiSign,"on position",move+1,".")
                printBoard()
        else:
            print("You Win. Congratulations !!!")
            break

game()

while True:
    choice=input("Do you want to play the game again ? (y/n) : ")
    if choice.lower()=="y":
        print("-"*30)
        board=[" " for x in range(9)]
        game()
    elif choice.lower()=="n":
        break
    else:
        print("Please enter a valid response.")
