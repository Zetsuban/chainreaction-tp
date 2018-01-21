from button			import *
from constants		import *
from text_zone		import *
from var_button		import *
from var_text		import *
from board			import *
from algorithms		import *

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

	try:
		f = open('chainreaction.save')
		f.close()
	except FileNotFoundError:
		with open('chainreaction.save', 'w') as f:
			f.writelines(world.player + "\n" + world.nbPlayer + "\n" + world.row + "\n" + world.col + "\n" + world.solo + "\n" + world.board + "\n" + world.turn)


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
	for i in (("M_NB_PLY_SLCT", PLAYER), ("M_NB_COL_SLCT", NB_COL),
				("M_NB_ROW_SLCT", NB_ROW)):
		world.all_object.add(text_zone_c(world.options["LANG"][i[0]], BLUE,
			T_MEDIUM, screen_center_x - 100, screen_center_y + (T_MEDIUM * (j - 1))))
		world.all_object.add(var_button_c(WHITE, T_MEDIUM,
			screen_center_x + 150, screen_center_y + (T_MEDIUM * (j - 1)),
			world.game_set[j], i[1]))
		j += 1
	world.all_object.add(button_c(world.options["LANG"]["B_START"], BLUE,
		T_MEDIUM, "START", screen_center_x, screen_center_y + (T_MEDIUM * j)))
	world.all_object.add(button_c(world.options["LANG"]["B_BACK"], BLUE,
		T_MEDIUM, "BACK", screen_center_x, world.options["HEIGHT"] - T_MEDIUM))

def start_game(world):

	if world.all_object:
		world.all_object.clear(world.screen, world.background)
		world.all_object.empty()
	else:
		world.all_object = pygame.sprite.Group()

	world.all_object.add(button_c(world.options["LANG"]["B_SAVE_&_BACK"], BLUE,
		T_MEDIUM, "SAVE_&_BACK", T_MEDIUM / 2,
		world.options["HEIGHT"] - T_MEDIUM,
		"top_left"))
	world.all_object.add(var_text_c("TURN" , T_MEDIUM, BLUE,
						world.options["LANG"]["M_TURN"], 0, 0))
	world.all_object.add(var_text_c("PLAYER" , T_MEDIUM, BLUE,
						world.options["LANG"]["M_PLAYER"], T_MEDIUM, 0))
	world.all_object.add(board_c(world,
								newBoard(world.game_set[1], world.game_set[2]),
								(world.game_set[1], world.game_set[2]),
								world.game_set[0]))

# dummy function for the 'continue' button when no previous save is loaded
def dummy(world):
	pass

def end_game_screen(world):

	if world.all_object:
		world.all_object.clear(world.screen, world.background)
		world.all_object.empty()
	else:
		world.all_object = pygame.sprite.Group()

	screen_center_x = world.options["WIDTH"] / 2
	screen_center_y = world.options["HEIGHT"] / 2

	world.all_object.add(var_text_c("WINNER" , T_MEDIUM, BLUE,
						world.options["LANG"]["M_WINNER"],
						screen_center_x, screen_center_y, "center"))
	world.all_object.add(button_c(world.options["LANG"]["B_AGAIN"], BLUE,
		T_MEDIUM, "AGAIN", screen_center_x, screen_center_y + T_MEDIUM,
		"center"))
	world.all_object.add(button_c(world.options["LANG"]["B_EXIT"], BLUE,
		T_MEDIUM, "EXIT", screen_center_x, screen_center_y + (T_MEDIUM * 2),
		"center"))

def load_save(world):

	if world.all_object:
		world.all_object.clear(world.screen, world.background)
		world.all_object.empty()
	else:
		world.all_object = pygame.sprite.Group()

	world.all_object.add(button_c(world.options["LANG"]["B_SAVE_&_BACK"], BLUE,
								T_MEDIUM, "SAVE_&_BACK", T_MEDIUM / 2,
								world.options["HEIGHT"] - T_MEDIUM,
								"top_left"))
	world.all_object.add(var_text_c("TURN" , T_MEDIUM, BLUE,
						world.options["LANG"]["M_TURN"], 0, 0))
	world.all_object.add(var_text_c("PLAYER" , T_MEDIUM, BLUE,
						world.options["LANG"]["M_PLAYER"], T_MEDIUM, 0))
	game = board_c(world, world.board, (world.row, world.col), world.nbPlayer)
	game.current_player = world.player
	game.solo = world.solo
	game.turn = world.turn
	world.all_object.add(game)

def exit(world):
	world.running = False

B_FUNC = {
	"BACK"			: main_menu,
	"NEW_GAME" 		: game_mode_selection,
	"CONTINUE"	 	: load_save,
	"RULES" 		: rules,
	"CREDITS" 		: credits,
	"EXIT" 			: exit,
	"START" 		: start_game,
	"AGAIN"			: game_mode_selection,
	"SAVE_&_BACK"	: save_and_back,
	"NONE"			: dummy
}
