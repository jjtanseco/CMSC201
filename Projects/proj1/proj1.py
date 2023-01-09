# File: proj1.py
# Author: Joshua Julian Tanseco
# Date: 11/10/16
# Section: 18
# E-mail: tanseco1@umbc.edu
# Description:
# This program allows users to play connect 4. They can choose to
# start from a previous save or start a brand new game. At any point 
# during their turn, they are allowed to save their progress.
# Collaboration:
# Collaboration was not allowed on this assignment

# Global Constants
SHOOT_MIN = 1
LENGTH_MIN = 5

BLANK = "_"
PLAYER_1 = "X"
PLAYER_2 = "O"

WELCOME = "Welcome to Connect Four! \n This is a game for two players"

# askSize():  Asks user for preferred size of board
# INPUT:      a string, "row" or "column"
# OUTPUT:     an integer, Row or Column lengths
def askSize(rowCol):
    #aks user for number
    message = ("Please choose number of " + rowCol + \
                   "s (greater than or equal to " + str(LENGTH_MIN) + "): ")
    length = int(input(message))

    #Sentinel loop keeps asking until valid number
    while length < LENGTH_MIN:
        length = int(input(message))

    #returns length once valid
    return length



# createBoard(): creates the board in the form of a 2D list
# INPUT:         integers, a row and column length
# OUTPUT:        a 2D list, blank board
def createBoard(row, col):
    #creates empty board
    boardList = []
    
    #makes 2D list
    for line in range(row):
        #initial row of each line
        tempRow = []

        for element in range(col):
            tempRow.append("_")
        boardList.append(tempRow)

    return boardList



# printBoard(): prints the board in a 2d matrix
# INPUT:        2D list, the board
# OUTPUT:       none, prints the board to the screen
def printBoard(board):

    print("")
    for row in board: #row
        # print each element
        for element in row:
            print(element, end = " ")
        # print newline
        print("")
    print("")



#move():    function to have player move
#INPUT:     original board (list), True or false, length of the row
#OUTPUT:    the new board (list)
def move(boardList, player1):

    #establishes row length
    rowLength = len(boardList[1])


    # Decide which turn to use. Tells user who's turn it is
    if player1 == True:
        piece = PLAYER_1
        print("Player 1 what is your choice?")

    else:
        piece = PLAYER_2
        print("Player 2 what is your choice?")

    #asks where to place piece (and makes sure that it's over the row length
    message = ("Please choose a column to place your piece in (1 to " \
                   + str(rowLength) + ") or s to save: ")
    
    #sentinel to get valid input
    invalid = True

    while invalid:
        #get input
        colChoice = input(message)

        #check if it's s
        if colChoice == "s":
            
            #saves game
            save(boardList)

        #Check if it's between 1 and length
        elif int(colChoice) <= rowLength and int(colChoice) >= 1:
            
            invalid = False
            start = len(boardList) - 1
            stop  = -1
            step  = -1
            
            for row in range(start, stop, step):
                
                if boardList[row ][int(colChoice) - 1] == BLANK:
                    boardList[row ][int(colChoice) - 1] = piece
                    return

        #asks again if column is full
        invalid = True
        
        


#save()    Saves the board as a STRING file 
#INPUT:    a 2D list; The board
#OUTPUT:   none. 
def save(boardList):
    
    fileName = input("What game file would you like to save to? ")
    
    userFile = open(fileName, "w")


    #makes fake boardList to turn into string and save ;D
    tempBoardList = boardList

    #joins each row into a string
    for index in range(len(tempBoardList)):
        tempBoardList[index] = " ".join(tempBoardList[index])

    tempBoardList = "\n".join(tempBoardList)

    userFile.write(tempBoardList)
    
    userFile.close()


    
#load()    This program makes board list from a previously saved string
#INPUT:    NONE
#OUTPUT:   a 2D list; the board
def load():

    #asks for file name
    fileName = input("What game file would you like to load from? ")

    #opens file to read
    userFile = open(fileName, "r")

    #reads file
    fileList = userFile.readlines()

    for index in range(len(fileList)):
        fileList[index] = fileList[index].split()

    return fileList



#check()    This checks if anyone won or if tie
#INPUT:     a 2D list: the board; a boolean
#OUTPUT:    "player1" "player2" or "none"; the possible winners
def checkWinner(board, player1):

    if player1:
        piece = PLAYER_1


    else:
        piece = PLAYER_2

    #check if 4 in a row.
    for row in range(len(board)):

        for index in range(len(board[row])-3):

            horizontal = (board[row][index] == piece and \
                              board[row][index + 1] == piece and \
                              board[row][index + 2] ==piece and \
                              board[row][index + 3] == piece)

            if horizontal:

                print("it's horizontal")
                  #player 1 wins
                if player1:
                    return "player1"

                  #player 2
                else: 
                    return "player2"


    #checks if 4 vertical
    for row in range(len(board)-3):

        for index in range(len(board[row])):

            vertical  = (board[row][index] == piece and \
                             board[row + 1][index] ==piece and \
                             board[row + 2][index] == piece and \
                             board[row + 3][index] == piece)

            if vertical:

                print("it's vertical")
                if player1:
                    return "player1"

                else:
                    return "player2"
    

    #Diagonal going down to the right
    for row in range(len(board)-3):

        for index in range(len(board[row])-3):

            diagonalDown = (board[row][index] == piece and \
                        board[row + 1][index + 1] == piece and \
                        board[row + 2][index + 2] == piece and \
                        board[row + 3][index + 3] == piece)

            if diagonalDown:
                print("it's diagonal down")
                if player1:
                    return "player1"

                else:
                    return "player2"

    #Diagonal going down to the left
    for row in range(2, len(board)):

        for index in range(len(board[row])-3):

            diagonalUp = (board[row][index] == piece and \
                              board[row - 1][index + 1] == piece and \
                              board[row - 2][index + 2] == piece and \
                              board[row - 3][index + 3] == piece)

            if diagonalUp:

                print("It's diagonal Up")
                if player1:
                    return "player1"

                else:
                    return "player2"

    return "none"



#checkTie:    Checks to see if all spaces are filled
#INPUT:       a 2D list; the board
#OUTPUT:      True or False; whether there is a winner or not.
def checkTie(boardList):

    for row in boardList:
        for item in row:
            if item == BLANK:
                return False

    return True


# countPieces():    Counts how many pieces are currently on the board
# INPUT:            a 2D list; the board
# OUTPUT:           an integer: how many pieces are on the board
def countPieces(board):

    pieceCount = 0

    for row in board:

        for item in row:

            if item != BLANK:
                pieceCount += 1
    return pieceCount






def main():

    print(WELCOME)

    #asks player if they want to load a game
    loadMessage = "Would you like to load a game (y/n)? "
    y = "y"
    n = "n"

    loadGame = input(loadMessage)
    while loadGame != y and loadGame != n:
        loadGame = input(loadMessage)

    #sets boardList to loaded game if they choose y
    if loadGame == y:
        boardList = load()

        #determines which piece goes first.
        pieceAmount = countPieces(boardList)
        if (pieceAmount % 2) == 0:
            player1 = True

        else:
            player1 == False


    #sets boardList to whatever lengths they chooose
    elif loadGame == n:

        #asks for row length
        rowLength = int(askSize("row"))

        #asks for column length
        colLength = int(askSize("column"))

        #uses t
\hose lengths to make 2D List (board) and sets it to boardList
        boardList = createBoard(rowLength, colLength)

        #sets player 1's turn
        player1 = True


    replay = "y"

    while replay == "y":

        #starts FIRST turn (prints the board then asks player to make move
        printBoard(boardList)
        move(boardList, player1)
    
        #prints board
        printBoard(boardList)

        #checks if winner or tie
        winner = checkWinner(boardList, player1)
        tie = checkTie(boardList)

        #switches player
        player1 = False

        #loops until winner is decided
        while winner == "none" and tie == False:

            #let's player make move
            move(boardList, player1)

            #prints board again
            printBoard(boardList)

            #checks again for winner
            winner = checkWinner(boardList, player1)
            #and for tie
            tie = checkTie(boardList)

            #switches player
            if player1 == True:
                player1 = False
            else:
                player1 = True
    
        #prints winner
        if winner != "none":

            if winner == "player1":
                print("Player 1 wins!")

            else:
                print("Player 2 wins!")

        #prints tie
        else:
            print("It's a draw!")

        #asks player if they want to play again
        replay = input("Would you like to play again? (y/n)? ")

        while replay != "y" and replay != "n":

            replay =input("Would you like to play again? (y/n)? ")


        #build board again if they want to replay
        if replay == "y":

            #asks for row length
            rowLength = int(askSize("row"))

            #asks for column length
            colLength = int(askSize("column"))

            #uses those lengths to make 2D List (board) and sets it to boardList
            boardList = createBoard(rowLength, colLength)

            #sets player 1's turn
            player1 = True


main()
