### format of the list
- a board of x row & y col
- board[i][j] = (number_of_pawn, number_of_the_player)

### if move possible
- get list of changes
a list of all future state in an animation
a state contains a list of all box changed
box = ((posx, posy), player, nb_pawn)
