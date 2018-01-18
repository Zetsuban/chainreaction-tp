from random import randint
from itertools import repeat

# Create the board at the start of the game
def newBoard(col, row):
    gameBoard = []
    for i in range(row):
        boardRow = []
        for j in range(col):
            boardRow.append("00")
        gameBoard.append(boardRow)
    return gameBoard

# Check if a movement is possible
def possible(gameBoard, col, row, selCol, selRow, player):
    if gameBoard[selRow][selCol][1] == "0" or gameBoard[selRow][selCol][0] == str(player):
        return True
    return False
# This function isn't used since the verification is made in the graphical part but I still let it here since it was asked

# Test Print in console for test purpose
def cli_print(board, row, col):
	print(" " * 6, ("  " if int(len(str(col))) == 1 else "  ").\
		join(str(col_number) for col_number in range(1, col + 1)))
	print(" " * 4, "-" * (col * 3))
	for row_number in range(1, row + 1):
		print((" " if int(len(str(row_number))) == 1 else ""),
		row_number, ":",
				" ".join(str(box) for box in board[row_number - 1]))

# Get the adjacents cell
def adjacentFunc(maxRow, maxCol):
    adjacents = [[[] for j in repeat(None, maxCol)] for i in repeat(None, maxRow)]
    for row in range(maxRow):
        for col in range(maxCol):
            adjacentTmp = [[row + 1, col], [row - 1, col], [row, col + 1], [row, col - 1]]
            if row == 0:
                adjacentTmp.remove([row - 1, col])
            if row == maxRow - 1:
                adjacentTmp.remove([row + 1, col])
            if col == 0:
                adjacentTmp.remove([row, col - 1])
            if col == maxCol - 1:
                adjacentTmp.remove([row, col + 1])
            adjacents[row][col] = adjacentTmp
    return(adjacents)

# Main function for the game
def recursive_put(board, col, row, selCol, selRow, player, adjacent = None):

	if adjacent == None:
		adjacent = adjacentFunc(row, col)

	if (int(board[selRow][selCol][0])) >= len(adjacent[selRow][selCol]):
		board[selRow][selCol] = "00"
		for i in adjacent[selRow][selCol]:
			board[i[0]][i[1]] = str(int(board[i[0]][i[1]][0]) + 1) + str(player)
		for i in adjacent[selRow][selCol]:
			if int(board[i[0]][i[1]][0]) >= len(adjacent[i[0]][i[1]]):
				recursive_put(board, col, row, i[1], i[0], player, adjacent)

def ia(gameBoard, row, col, player):
    selRow = randint(0, row - 1)
    selCol = randint(0, col - 1)
    while not possible(gameBoard, col, row, selCol, selRow, player):
        selRow = randint(0, row - 1)
        selCol = randint(0, col - 1)
    return selRow, selCol

# Check if a player is still in game
def loose(gameBoard, col, row, player, turn ,nbPlayer):
    inGame = []
    for i in range(row):
        for j in range(col):
            inGame.append(gameBoard[i][j][0])
    if inGame.count(str(player)) == 0 and turn >= nbPlayer:
        return True
    return False

# Checks if number of player is more than 1 and if yes then this player is the winner
def win(gameBoard, col, row, player, nbPlayer, turn, playerList):
    for i in range(1,nbPlayer+1):
        if loose(gameBoard, col, row, i, turn, nbPlayer) == True:
            if playerList.count(i) > 0:
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

# Main function that launches every other one
# def launch(row, col, nbPlayer, saved):
#     playerList = [j for j in range(1,nbPlayer+1)]
#     solo = False
#     turn = 0
#     player = 1
#     gameBoard = newBoard(col,row)
#
#     if saves != None:
#         player = int(saves[0])
#         nbPlayer = int(saves[1])
#         row = int(saves[2])
#         col = int(saves[3])
#         solo = saves[4]
#         turn = int(saves[6])
#         gameBoard = saves[5].split()
#         for i in range(len(gameBoard)):
#             gameBoard[i] = gameBoard[i].split(",")
#
#     adjacents = adjacentFunc(row, col)
#     cli_print(gameBoard, row, col)
#
#     while not win(gameBoard, col, row, player, nbPlayer, turn, playerList):
#         if loose(gameBoard, col, row, player, turn, nbPlayer) == True:
#             player += 1
#         if player > nbPlayer:
#             player = playerList[0]
#         print("\nPlayer", player, "it's your turn")
#         selCol, selRow = playerInput() # Tes Input
#         put(gameBoard, col, row, selCol, selRow, player, adjacents)
#         print("\n")
#         cli_print(gameBoard, row, col) #Test Print
#         player = player % nbPlayer + 1
#         turn += 1
#         # for item in gameBoard:
#         #     writeSave.write("%s\n" % item)
#     winner = playerList[0]

# Main function for solo play
def launchSolo(row, col, saved):
    playerList = [1,2]
    solo = True
    nbPlayer = 2
    turn = 0
    player = 1
    gameBoard = newBoard(col,row)

    if saves != None:
        player = int(saves[0])
        nbPlayer = int(saves[1])
        row = int(saves[2])
        col = int(saves[3])
        solo = saves[4]
        turn = int(saves[6])
        gameBoard = saves[5].split()
        for i in range(len(gameBoard)):
            gameBoard[i] = gameBoard[i].split(",")

    adjacents = adjacentFunc(row, col)
    cli_print(gameBoard, row, col)

    while not win(gameBoard, col, row, player, nbPlayer, turn, playerList):
        if player == 2:
            selRow, selCol = ia(gameBoard, row, col, player)
        else:
            selCol, selRow = playerInput() # Tes Input
        put(gameBoard, col, row, selCol, selRow, player, adjacents)
        print("\n")
        cli_print(gameBoard, row, col) #Test Print
        player = (player % 2) + 1
        turn += 1
    winner = playerList[0]

def loadSave():
    loaded = False
    try:
        saveFile = open('chainreaction.sv', 'r')
        saves = saveFile.read().split('\n')
        saveFile.close()
        loaded = True
    except FileNotFoundError:
        return None
    if loaded == True:
        return saves


if __name__ == '__main__':
    solo = False
    row = 4
    col = 4
    nbPlayer = 3
    saved = True



    if saved == True:
        saves, nbPlayer, row, col, solo = continueGame()

    if nbPlayer < 2 or solo == True:
        launchSolo(col,row, saved)
    else:
        launch(row, col, nbPlayer, saved)
