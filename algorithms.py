def newBoard(col, row):
    gameBoard = []
    for i in range(col):
        boardRow = []
        for j in range(row):
            boardRow.append(0)
        gameBoard.append(boardRow)
    return gameBoard

def possible(gameBoard, col, row, selCol, selRow, player):
    return True if gameBoard[selCol][selRow] == player or gameBoard[selCol][selRow] == 0 else False

def put(gameBoard, col, row, selCol, selRow, player):
    gameBoard[selCol][selRow] = player
    # TODO: make the put fonction

def loose(gameBoard, col, row, player):
    if gameBoard.count(player) == 0:
        return True
    return False

def win(gameBoard, col, row, player, nbPlayer):
    trueCount = 0
    for i in range(nbPlayer):
        if loose(gameBoard, col, row, player) == False:
            trueCount += 1
            winner = i
    if trueCount > 1:
        return False
    print("Le Joueur", i, "remporte la partie")
    quit()

#Tmp function for test purpose
def playerInput():
    selCol = int(input("Colonne : "))
    selRow = int(input("Ligne : "))
    return selCol, selRow
##############################

def launch(col, row, nbPlayer):
    round = 0
    gameBoard = newBoard(col,row)
    player = 1
    #cli_print(gameBoard, col, row)
    while round < nbPlayer:
        if player > nbPlayer:
            player = 1
        selCol, selRow = playerInput()
        put(gameBoard, col, row, selCol, selRow, player)
        #cli_print(gameBoard, col, row)
        print(gameBoard) #Test Print
        player += 1
        round += 1
    while win(gameBoard, col, row, player, nbPlayer) == False:
        if loose(gameBoard, col, row, player) == True:
            player += 1
        if player > nbPlayer:
            player = 1
        selCol, selRow = playerInput()
        put(gameBoard, col, row, selCol, selRow, player)
        #cli_print(gameBoard, col, row)
        print(gameBoard) #Test Print
        player += 1

if __name__ == '__main__':
    col = int(input("board col : "))
    row = int(input("board row : "))
    nbPlayer = int(input("nbPlayer : "))
    launch(col,row,nbPlayer)
