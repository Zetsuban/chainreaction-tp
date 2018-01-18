import board

# Text size
T_BIG		= 100
T_MEDIUM	= 50
T_SMALL		= 25

# COLOR		  (  R,   G,   B)
WHITE		= (255, 255, 255)
BLACK		= (  0,   0,   0)
L_GRAY		= (200, 200, 200)
M_GRAY		= (128, 128, 128)
D_GRAY		= ( 50,  50,  50)
BLUE		= (  0,   0, 255)
RED			= (255,   0,   0)
MAGENTA		= (255,   0, 255)
GREEN		= (  0, 255,   0)
YELLOW		= (255, 255,   0)
D_BLUE		= (  0,   0, 128)
D_MAGENTA	= (128,   0, 128)
D_GREEN		= (  0, 128,   0)
D_YELLOW	= (128, 128,   0)

# color of different players
COLOR_PLAYER = (
BLUE, GREEN, YELLOW, MAGENTA,
D_BLUE, D_GREEN, D_YELLOW, D_MAGENTA
)

# french texts
LANG_FR = {
"RULES"			: (	"Règle :",
					"· Une partie est jouée par 2 à 8 joueurs",
					"· Chaque case peut comporter autant de pions qu'elle",
					"possède de cases adjacentes.",
					"",
					"Déroulement :",
					"· Chacun son tour, chaque joueur pourra poser un pion",
					"sur une case vide ou comportant déjà un ou plusieurs de",
					"ses pions.",
					"· Lorsque le nombre de pions sur une case est égale au",
					"nombre maximal de pions que celle ci peut comporter,",
					"chaque pion est envoyé sur une case adjacente.",
					"· Quand un pion est envoyé sur une case adjacente",
					"il capture et s'ajoute au.x pion.s déjà sur cette case.",
					"· Après que les pions se soient déplacés, si les cases",
					"adjacentes possèdent le nombre maximal de pions alors les",
					"pions se répartissent de nouveau et ainsi de suite",
					"jusqu'à ce qu'aucune case ne contienne son nombre maximal",
					"de pions.",
					"",
					"Condition de Victoire",
					"· L'objectif du jeu est d'éliminer les autres joueurs en",
					"capturant tout leurs pions."),
"CREDITS"		: (	"Crédits",
					"",
					"Chain-reaction"
					"",
					"Un projet par",
					"",
					"Arthur Froger",
					"&",
					"Joshua Menanteau"),
"M_SOLO_GM"		: ("Joueur VS IA",),
"M_MULTI_GM"	: ("Joueur VS Joueur",),
"M_NB_PLY_SLCT"	: ("Nombre de Joueurs",),
"M_NB_COL_SLCT"	: ("Nombre de colone",),
"M_NB_ROW_SLCT"	: ("Nombre de ligne",),
"M_TURN"		: "Tours  : ",
"M_PLAYER"		: "Joueur : ",
"B_BACK"		: "Retour",
"B_NEW_GAME"	: "Nouvelle Parti",
"B_CONTINUE"	: "Continuer",
"B_RULES"		: "Règle",
"B_CREDITS"		: "Crédit",
"B_EXIT"		: "Quitter",
"B_START"		: "Commencer",
"B_AGAIN"		: "Recommencer",
"B_SAVE_&_BACK"	: "Sauvegarder et Quitter",
"B_NONE"		: "Continuer"
}

# english texts
LANG_EN = {
"RULES"			: (	"Rules",
					"· A game can be played by 2 to 8 players",
					"· Each cell can contain as many piece as it has nearby",
					"cell",
					"",
					"Turn Sequence",
					"· Each turn, each player will be able to put down a piece",
					"on a cell of the board that holds none or one of his",
					"piece.",
					"· When the number of piece on a cell is equal to the",
					"maximum number that this one can hold, each pieces are",
					"individually send on the adjacent cell.",
					"· When a piece is send to a nearby cell, it capture and",
					" adds itself to the present piece(s).",
					"· If a piece has just been sent and the cell it is now on",
					"now contains the maximum number of pieces it can contains",
					"then the pices get send again until no cell contains the",
					"maximum number of cell."
					"",
					"Victory",
					"· A player is proclaimed winner when he is the last one",
					"to have pieces on the board."),
"CREDITS"		: (	"Credits",
					"",
					"Chain-reaction"
					"",
					"A project by",
					"",
					"Arthur Froger",
					"&",
					"Joshua Menanteau"),
"M_SOLO_GM"		: ("Player VS AI",),
"M_MULTI_GM"	: ("Player VS Player",),
"M_NB_PLY_SLCT"	: ("Number of player",),
"M_NB_COL_SLCT"	: ("Number of column",),
"M_NB_ROW_SLCT"	: ("Number of row",),
"M_TURN"		: "Turns  : ",
"M_PLAYER"		: "Player : ",
"B_BACK"		: "Back",
"B_NEW_GAME"	: "New Game",
"B_CONTINUE"	: "Continue",
"B_RULES"		: "Rules",
"B_CREDITS"		: "Credits",
"B_EXIT"		: "Exit",
"B_START"		: "Start",
"B_AGAIN"		: "Play Again",
"B_SAVE_&_BACK"	: "Save and Quit",
"B_NONE"		: "Continue"
}

# default general settings
DEFAULT = {
"HEIGHT"	: 720,
"WIDTH"		: 1280,
"LANG"		: LANG_EN
}

try:
	f = open('config.cfg')
	conf = f.read().split('\n')
	if conf[2] == "LANG_FR" or conf[2] == "LANG_EN":
		OPTION = {"HEIGHT" : int(conf[0]),"WIDTH" : int(conf[1]),"LANG" : eval(conf[2])}
	f.close()
	return OPTION
except FileNotFoundError:
	with open('test.txt', 'w') as f:
		f.writelines(str(DEFAULT["HEIGHT"])+"\n"+str(DEFAULT["WIDTH"])+"\n"+str(DEFAULT["LANG"]))

# limites for the number of player and dimension of the board
GAME_SETTINGS_LIMITE = ((1, 8), (4, 20), (4, 20))

# var_type for var_button_c
PLAYER = 0
NB_ROW = 1
NB_COL = 2

# var_type for var_text_c
VAR_TYPE = {
"TURN"		: board.board_c,
"PLAYER"	: board.board_c
}
turn			= 2
current_player	= 0
VAR = {
"TURN"		: "turn",
"PLAYER"	: "current_player"
}
