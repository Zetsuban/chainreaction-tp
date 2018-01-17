#
# Create the board at the start of the game
#
def newBoard(col, row):
    gameBoard = []
    for i in range(row):
        boardRow = []
        for j in range(col):
            boardRow.append("00")
        gameBoard.append(boardRow)
    return gameBoard

#
# Check if a movement is possible
#
def possible(gameBoard, col, row, selCol, selRow, player):
    if gameBoard[selRow][selCol][1] == "0" or gameBoard[selRow][selCol][0] == str(player):
        return True
    return False

#
# Test Print in console for test purpose
#
def cli_print(board, row, col):
	print(" " * 6, ("  " if int(len(str(col))) == 1 else "  ").\
		join(str(col_number) for col_number in range(1, col + 1)))
	print(" " * 4, "-" * (col * 3))
	for row_number in range(1, row + 1):
		print((" " if int(len(str(row_number))) == 1 else ""),
		row_number, ":",
				" ".join(str(box) for box in board[row_number - 1]))

#
# Main function for the game
#
def put(gameBoard, col, row, selCol, selRow, player):
    pion = gameBoard[selRow][selCol]
    gameBoard[selRow][selCol] = str(player) + str(int(pion[1]) + 1)
    pion = gameBoard[selRow][selCol]

    # First make a list of the adjacent cells
    # Then "overflow" to all neighbors
    adjacent = []
    if selRow == 0:
        adjacent.append([selRow + 1, selCol])
    if selRow == row - 1:
        adjacent.append([selRow - 1, selCol])
    else:
        adjacent.append([selRow + 1, selCol])
        adjacent.append([selRow - 1, selCol])
    if selCol == 0:
        adjacent.append([selRow, selCol + 1])
    if selCol == col -1:
        adjacent.append([selRow, selCol - 1])
    else:
        adjacent.append([selRow, selCol + 1])
        adjacent.append([selRow, selCol - 1])

    print(adjacent)

    # if not adjacent: # Then the selected cell has 4 border
    #     #print('else')
    #     if int(pion[1]) == 4:
    #         gameBoard[selRow + 1][selCol] = str(player) + str(int(gameBoard[selRow + 1][selCol][1]) + 1)
    #         gameBoard[selRow][selCol + 1] = str(player) + str(int(gameBoard[selRow][selCol + 1][1]) + 1)
    #         gameBoard[selRow - 1][selCol] = str(player) + str(int(gameBoard[selRow - 1][selCol][1]) + 1)
    #         gameBoard[selRow][selCol - 1] = str(player) + str(int(gameBoard[selRow][selCol - 1][1]) + 1)
    #         gameBoard[selRow][selCol] = "00"


    # # Detect that the selected case is in an angle : The cell has 2 border
    # if (selRow == 0 and selCol == 0) or (selRow == 0 and selCol == col)\
    #  or (selRow == row and selCol == 0) or (selRow == row and selCol == col):
    #     print(pion[1])
    #     if int(pion[1]) == 2:
    #         if (selRow == 0 and selCol == 0):
    #             gameBoard[selRow + 1][selCol] = str(player) + str(int(gameBoard[selRow + 1][selCol][1]) + 1)
    #             gameBoard[selRow][selCol + 1] = str(player) + str(int(gameBoard[selRow][selCol + 1][1]) + 1)
    #             gameBoard[selRow][selCol] = "00"
    #         elif (selRow == 0 and selCol == col):
    #             gameBoard[selRow + 1][selCol] = str(player) + str(int(gameBoard[selRow + 1][selCol][1]) + 1)
    #             gameBoard[selRow][selCol - 1] = str(player) + str(int(gameBoard[selRow][selCol - 1][1]) + 1)
    #             gameBoard[selRow][selCol] = "00"
    #         elif (selRow == row and selCol == 0):
    #             gameBoard[selRow - 1][selCol] = str(player) + str(int(gameBoard[selRow - 1][selCol][1]) + 1)
    #             gameBoard[selRow][selCol + 1] = str(player) + str(int(gameBoard[selRow][selCol + 1][1]) + 1)
    #             gameBoard[selRow][selCol] = "00"
    #         elif (selRow == row and selCol == col):
    #             gameBoard[selRow - 1][selCol] = str(player) + str(int(gameBoard[selRow - 1][selCol][1]) + 1)
    #             gameBoard[selRow][selCol - 1] = str(player) + str(int(gameBoard[selRow][selCol - 1][1]) + 1)
    #             gameBoard[selRow][selCol] = "00"
    #
    # # Detect that a cell is on a border but not an angle : The cell has 3 border
    # elif (selCol > 0 and selCol < col and selRow == 0)\
    #  or (selRow == row and selCol > 0 and selCol < col)\
    #  or (selCol == 0 and selRow > 0 and selRow < row)\
    #  or (selCol == col and selRow > 0 and selRow < row):
    #     #print('eliff')
    #     if int(pion[1]) == 3:
    #         if selRow == 0:
    #             gameBoard[selRow + 1][selCol] = str(player) + str(int(gameBoard[selRow + 1][selCol][1]) + 1)
    #             gameBoard[selRow][selCol + 1] = str(player) + str(int(gameBoard[selRow][selCol + 1][1]) + 1)
    #             gameBoard[selRow][selCol - 1] = str(player) + str(int(gameBoard[selRow][selCol - 1][1]) + 1)
    #             gameBoard[selRow][selCol] = "00"
    #         elif selRow == row - 1:
    #             gameBoard[selRow - 1][selCol] = str(player) + str(int(gameBoard[selRow - 1][selCol][1]) + 1)
    #             gameBoard[selRow][selCol + 1] = str(player) + str(int(gameBoard[selRow][selCol + 1][1]) + 1)
    #             gameBoard[selRow][selCol - 1] = str(player) + str(int(gameBoard[selRow][selCol - 1][1]) + 1)
    #             gameBoard[selRow][selCol] = "00"
    #         elif selCol == 0:
    #             gameBoard[selRow + 1][selCol] = str(player) + str(int(gameBoard[selRow + 1][selCol][1]) + 1)
    #             gameBoard[selRow - 1][selCol] = str(player) + str(int(gameBoard[selRow - 1][selCol][1]) + 1)
    #             gameBoard[selRow][selCol + 1] = str(player) + str(int(gameBoard[selRow][selCol + 1][1]) + 1)
    #             gameBoard[selRow][selCol] = "00"
    #         elif selCol == col - 1:
    #             gameBoard[selRow + 1][selCol] = str(player) + str(int(gameBoard[selRow + 1][selCol][1]) + 1)
    #             gameBoard[selRow - 1][selCol] = str(player) + str(int(gameBoard[selRow - 1][selCol][1]) + 1)
    #             gameBoard[selRow][selCol - 1] = str(player) + str(int(gameBoard[selRow][selCol - 1][1]) + 1)
    #             gameBoard[selRow][selCol] = "00"
    #
    # else: # Then the selected cell has 4 border
    #     #print('else')
    #     if int(pion[1]) == 4:
    #         gameBoard[selRow + 1][selCol] = str(player) + str(int(gameBoard[selRow + 1][selCol][1]) + 1)
    #         gameBoard[selRow][selCol + 1] = str(player) + str(int(gameBoard[selRow][selCol + 1][1]) + 1)
    #         gameBoard[selRow - 1][selCol] = str(player) + str(int(gameBoard[selRow - 1][selCol][1]) + 1)
    #         gameBoard[selRow][selCol - 1] = str(player) + str(int(gameBoard[selRow][selCol - 1][1]) + 1)
    #         gameBoard[selRow][selCol] = "00"


def loose(gameBoard, col, row, player, turn ,nbPlayer):
    currentPlayerList = []
    for i in range(row):
        for j in range(col):
            currentPlayerList.append(gameBoard[i][j][0])
    if currentPlayerList.count(str(player)) == 0 and turn >= nbPlayer:
        return True
    return False

def win(gameBoard, col, row, player, nbPlayer, turn, playerList):
    for i in range(nbPlayer):
        if loose(gameBoard, col, row, i, turn, nbPlayer) == True:
            playerList.remove(i)
    if len(playerList) > 1:
        return False
    return True

#Tmp function for test purpose
def playerInput():
    selRow = int(input("Ligne : ")) - 1
    selCol = int(input("Colonne : ")) - 1
    return selCol, selRow
##############################

def launch(col, row, nbPlayer):
    playerList = []
    for i in range(1,nbPlayer+1):
        playerList.append(i)

    turn = 0
    gameBoard = newBoard(col,row)
    player = 1
    cli_print(gameBoard, row, col)
    #print(gameBoard)

    while win(gameBoard, col, row, player, nbPlayer, turn, playerList) == False:
        if loose(gameBoard, col, row, player, turn, nbPlayer) == True:
            player += 1
        print("\nPlayer", player, "it's your turn")
        selCol, selRow = playerInput()
        put(gameBoard, col, row, selCol, selRow, player)
        print("\n")
        cli_print(gameBoard, row, col) #Test Print
        player = player % nbPlayer + 1
        turn += 1
    print("player", player + 1, "wins")

if __name__ == '__main__':
    #col = int(input("board col : "))            #
    #row = int(input("board row : "))            # Will be inported from gui
    #nbPlayer = int(input("nbPlayer : "))        #
    row = 4
    col = 4
    nbPlayer = 2
    launch(col,row,nbPlayer)
