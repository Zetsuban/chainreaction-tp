def newBoard(col, row):
    gameBoard = []
    for i in range(col):
        boardRow = []
        for j in range(row):
            boardRow.append(0)
        gameBoard.append(boardRow)
    return gameBoard

def cli_print(gameBoard, col, row):
	print(" " * 5, (" " if int(len(str(col))) == 1 else "  ").\
		join(str(col_number) for col_number in range(1, col + 1)))
	print(" " * 4, "-" * (col * 3))
	for row_number in range(1, row + 1):
		print((" " if int(len(str(row_number))) == 1 else ""),
		row_number, ":",
				" ".join(box for box in gameBoard[row_number - 1]))

def possible(gameBoard, col, row, selCol, selRow, player):
    if gameBoard[selCol][selRow] == player or gameBoard[selCol][selRow] == 0:
        return True
    return False

def put(gameBoard, col, row, selCol, selRow, player):
    # TODO: make the put fonction
    print("test")

def loose(gameBoard, col, row, player):
    if gmaeboard.count(player) == 0:
        return True
    return False

def win(gameBoard, col, row, player):
    # TODO: Find a way to check every player and if all excet one return true from the loose function then that player wins
    print("test")

#Tmp function for test purpose
def playerInput():
    selCol = int(input("Colonne : "))
    selrow = int(input("Ligne : "))
    return selCol, selrow
##############################

def launch(col, row, nbPlayer):
    gameBoard = newBoard(col,row)
    player = 1
    cli_print(gameBoard, col, row)
    while win(gameBoardcol,row,player) == False:
        if loose(gameBoard, col, row, player) == True:
            player += 1
        if player >= nbPlayer:
            player = 1
        selCol, selRow = input()
        put(gameBoard, col, row, player)
        cli_print(gameBoard, col, row)
        player += 1

if __name__ == '__main__':
    col = int(input("board col : "))
    row = int(input("board row : "))
    nbPlayer = int(input("nbPlayer : "))
    launch(col,row,nbPlayer)
