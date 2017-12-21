# n = col
# m = row

def newBoard(col,row):
    gameBoard = []
    for i in range(col):
        row = []
        for j in range(row):
            row.append(0)
        board.append(row)
    return gameBoard

def possible(gameBoard,col,row,selCol,selRow,player):
    if gameBoard[selCol][selRow] == player or gameBoard[selCol][selRow] == 0:
        return True
    return False

def put(gameBoard,col,row,selCol,selRow,player):
    # TODO: make the put fonction

def loose(gameBoard,col,row,player):
    if gmaeboard.count(player) == 0:
        return True
    return False

def win(gameBoard,col,row,player):
    # TODO: Find a way to check every player and if all excet one return true from the loose function then that player wins

#Tmp function for test purpose
def input():
    selCol = int(input("Colonne : "))
    selrow = int(input("Ligne : "))
##############################

def launch():
    newBoard(col,row)
    while win(gameBoardcol,row,player) == False:


if __name__ == '__main__':
    col = int(input("board col : "))
    row = int(input("board row : "))
