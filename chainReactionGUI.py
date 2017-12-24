import sys
import pygame
from pygame.locals import *

from classes import *


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

WHITE	= (255, 255, 255)
RED		= (255,   0,   0)
MARROON	= (128,   0,   0)

COLOR_PLAYER = (
(255, 0, 0),	(0, 255, 0),	(0, 0, 255),
(128, 0, 0),	(0, 128, 0),	(0, 0, 128),
(255, 255, 0),	(0, 255, 255)
)

#
# main
#

def main():

    # load_cfg()
    # save = load_save()

	screen = pygame.display.set_mode((1280,720))
	main_menu(screen)




#
# game loop
#

#
# main menu loop
#

def main_menu(screen):

	running = True

	buttons = pygame.sprite.Group()

	new_game = button_c("New Game", RED, 50, "NEW_GAME", 1280 / 2, 20)

	buttons.add(new_game)

	while running:
		screen.fill(WHITE)
		buttons.update(pygame.mouse.get_pos())
		buttons.draw(screen)
		pygame.display.flip()

		for event in pygame.event.get():
			if event.type == QUIT:
				return
			if event.type == MOUSEBUTTONUP:
				buttons.update(pygame.mouse.get_pos(), True)



#
# Credit
#
def credits():
	pass

#
# RULES
#
def rules():
	pass

#
# save
#

#
# load cfg/save
#
def save_and_back():
	pass

#
# game mode menu
#
def game_mode_selection():
	print("toto est rigolo")
	pass

def start_game():
	pass

# dummy function for the 'continue' button when no previous save is loaded
def dummy():
	pass

def exit():
	pass

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
