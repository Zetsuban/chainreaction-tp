
# display board in such a fashion
# |       1  2  3  4  5 20
# |    -------------------
# |  1 : 0B 2R 2V 2F 2Z 2E
# |  1 :
# |  1 :
# |  1 :
# | 20 :
def cli_print(board, row, col):

	print(" " * 5, (" " if int(len(str(col))) == 1 else "  ").\
		join(str(col_number) for col_number in range(1, col + 1)))
	print(" " * 4, "-" * (col * 3))
	for row_number in range(1, row + 1):
		print((" " if int(len(str(row_number))) == 1 else ""),
		row_number, ":",
				" ".join(box for box in board[row_number - 1]))


#
# menu GUI
#


#
# game GUI
#
