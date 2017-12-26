from button		import *
from constants	import *

# kill world.all_object if != None add button object to all_object
def main_menu(world):
	if world.all_object:
		world.all_object.empty()
	else:
		world.all_object = pygame.sprite.Group()

	screen_center_x = world.options["WIDTH"] / 2

	j = 0
	for i in ("NEW_GAME", "CONTINUE", "RULES", "CREDITS", "EXIT"):
		world.all_object.add(button_c(world.options["LANG"]["B_" + i], BLUE,
							T_MEDIUM, i, screen_center_x, 200 + T_MEDIUM * j))
		j += 1

	print("main_menu")

#
# Credit
#
def credits(world):
	print("credits")

#
# RULES
#
def rules(world):
	print("rules")

#
# save
#

#
# load cfg/save
#
def save_and_back(world):
	print("save_and_back")

#
# game mode menu
#
def game_mode_selection(world):
	print("game_mode_selection")


def start_game(world):
	print("start_game")

# dummy function for the 'continue' button when no previous save is loaded
def dummy(world):
	print("dummy")

def exit(world):
	world.running = False

B_FUNC = {
	"BACK"			: main_menu,
	"NEW_GAME" 		: game_mode_selection,
	"CONTINUE"	 	: start_game,
	"RULES" 		: rules,
	"CREDITS" 		: credits,
	"EXIT" 			: exit,
	"START" 		: start_game,
	"AGAIN"			: game_mode_selection,
	"SAVE_&_BACK"	: save_and_back,
	"NONE"			: dummy
}
