from button		import *
from constants	import *
from text_zone	import *

def main_menu(world):

	if world.all_object:
		world.all_object.empty()
	else:
		world.all_object = pygame.sprite.Group()

	screen_center_x = world.options["WIDTH"] / 2
	screen_center_y = world.options["HEIGHT"] / 2

	j = 0
	for i in ("NEW_GAME", "CONTINUE" if world.save else "NONE",
				"RULES", "CREDITS", "EXIT"):
		world.all_object.add(button_c(world.options["LANG"]["B_" + i], BLUE,
			T_BIG, i, screen_center_x, screen_center_y + T_BIG * (j - 2)))
		j += 1

def credits(world):

	if world.all_object:
		world.all_object.clear(world.screen, world.background)
		world.all_object.empty()
	else:
		world.all_object = pygame.sprite.Group()

	screen_center_x = world.options["WIDTH"] / 2
	world.all_object.add(button_c(world.options["LANG"]["B_BACK"], BLUE,
		T_MEDIUM, "BACK", screen_center_x, world.options["HEIGHT"] - T_MEDIUM))
	world.all_object.add(text_zone_c(world.options["LANG"]["CREDITS"], BLUE,
		T_MEDIUM, screen_center_x,
		T_MEDIUM * (len(world.options["LANG"]["CREDITS"]) + 1) / 1.5, "center"))

def rules(world):

	if world.all_object:
		world.all_object.clear(world.screen, world.background)
		world.all_object.empty()
	else:
		world.all_object = pygame.sprite.Group()

	screen_center_x = world.options["WIDTH"] / 2
	world.all_object.add(button_c(world.options["LANG"]["B_BACK"], BLUE,
		T_MEDIUM, "BACK", screen_center_x, world.options["HEIGHT"] - (T_MEDIUM / 2)))
	world.all_object.add(text_zone_c(world.options["LANG"]["RULES"], BLUE,
		T_SMALL, screen_center_x,
		T_SMALL * (len(world.options["LANG"]["RULES"]) + 1) / 1.5))

def save(world):
	pass

def save_and_back(world):
	save(world)
	main_menu(world)

def game_mode_selection(world):

	if world.all_object:
		world.all_object.clear(world.screen, world.background)
		world.all_object.empty()
	else:
		world.all_object = pygame.sprite.Group()

	screen_center_x = world.options["WIDTH"] / 2
	screen_center_y = world.options["HEIGHT"] / 2
	j = 0
	for i in ("M_NB_PLY_SLCT", "M_NB_COL_SLCT", "M_NB_ROW_SLCT"):
		world.all_object.add(text_zone_c(world.options["LANG"][i], BLUE,
			T_MEDIUM, screen_center_x, screen_center_y + (T_MEDIUM * (j - 1))))
		j += 1
	world.all_object.add(button_c(world.options["LANG"]["B_BACK"], BLUE,
		T_MEDIUM, "BACK", screen_center_x, world.options["HEIGHT"] - T_MEDIUM))

def start_game(world):
	print("start_game")

# dummy function for the 'continue' button when no previous save is loaded
def dummy(world):
	pass

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
