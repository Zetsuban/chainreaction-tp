from random import randint
from itertools import repeat

# Create the board at the start of the game
def newBoard(row, col):
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
def recursive_put(board, col, row, selCol, selRow, player, playerList, adjacent = None):

	if adjacent == None:
		adjacent = adjacentFunc(row, col)

	if (int(board[selRow][selCol][0])) >= len(adjacent[selRow][selCol]):
		board[selRow][selCol] = "00"
		for i in adjacent[selRow][selCol]:
			board[i[0]][i[1]] = str(int(board[i[0]][i[1]][0]) + 1) + str(player)
		for i in adjacent[selRow][selCol]:
			if int(board[i[0]][i[1]][0]) >= len(adjacent[i[0]][i[1]]):
				return(recursive_put(board, col, row, i[1], i[0], player, playerList, adjacent))

# AI's brain
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
            inGame.append(gameBoard[i][j][1])
    if inGame.count(str(player)) == 0 and turn > nbPlayer:
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

def loadSave():
	loaded = False
	try:
		saveFile = open('chainreaction.save', 'r')
		saves = saveFile.read().split('\n')
		if len(saves) >= 7:
			loaded = True
		saveFile.close()
	except FileNotFoundError:
		return None

	return(saves if loaded else None)
