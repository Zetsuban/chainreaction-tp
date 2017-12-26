import sys
import pygame
from pygame.locals import *

from classes			import *
from GUI_classes_test	import *
from constants			import *

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
# main
#

def main():

    # load_cfg()
    # save = load_save()

	game = game_c(DEFAULT)
	game.world_loop()


#
# game loop
#

#
# main menu loop
#

# def main_menu(screen):
#
# 	running = True
#
# 	buttons = pygame.sprite.Group()
#
# 	new_game = button_c("New Game", RED, 50, "NEW_GAME", 1280 / 2, 20)
#
# 	buttons.add(new_game)
#
# 	while running:
# 		screen.fill(WHITE)
# 		buttons.update(pygame.mouse.get_pos())
# 		buttons.draw(screen)
# 		pygame.display.flip()
#
# 		for event in pygame.event.get():
# 			if event.type == QUIT:
# 				return
# 			if event.type == MOUSEBUTTONUP:
# 				buttons.update(pygame.mouse.get_pos(), True)


# kill world.all_object if != None add button object to all_object
def main_menu(world):
	if world.all_object:
		world.all_object.empty()

	new_game_button = button_c(world.options["LANG"]["B_NEW_GAME"], BLUE,
						50, "NEW_GAME", world.options["WIDTH"] / 2, 100)
	world.all_object.add(new_game_button)

	print("main_menu")

#
# Credit
#
def credits():
	print("credits")

#
# RULES
#
def rules():
	print("rules")

#
# save
#

#
# load cfg/save
#
def save_and_back():
	print("save_and_back")

#
# game mode menu
#
def game_mode_selection():
	print("game_mode_selection")


def start_game():
	print("start_game")

# dummy function for the 'continue' button when no previous save is loaded
def dummy():
	print("dummy")

def exit():
	print("exit")

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
