import sys
import pygame
from pygame.locals import *

from world		import *
from constants	import *
from algorithms import *
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

# Config File
def configFunc():
	okay = False
	OPTION = {}
	try:
		f = open('config.cfg', 'r')
		conf = f.read().split('\n')
		if (conf[2] == "LANG_FR" or conf[2] == "LANG_EN") and (RESOLUTION.count([int(conf[0]), int(conf[1])]) == 1):
			OPTION = {"HEIGHT" : int(conf[1]),"WIDTH" : int(conf[0]),"LANG" : eval(conf[2])}
		f.close()
		okay = True
	except FileNotFoundError:
		with open('test.txt', 'w') as f:
			f.writelines(str(DEFAULT["HEIGHT"])+"\n"+str(DEFAULT["WIDTH"])+"\n"+str(DEFAULT["LANG"]))

	return(OPTION if okay else DEFAULT)



#
# main
#

def main():
	options = configFunc()
	save = loadSave()

	game = game_c(options, save)
	game.world_loop()

if __name__ == '__main__':
	try:
		pygame.init()
		main()
		pygame.quit()
	except EOFError:
		sys.exit(-1)
	except KeyboardInterrupt:
		sys.exit(-1)
	else:
		sys.exit(0)
