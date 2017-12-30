# Text size
T_BIG		= 100
T_MEDIUM	= 50
T_SMALL		= 25

# COLOR		  (  R,   G,   B)
WHITE		= (255, 255, 255)
BLACK		= (  0,   0,   0)
BLUE		= (  0,   0, 255)
MAGENTA		= (255,   0, 255)
GREEN		= (  0, 255,   0)
YELLOW		= (255, 255,   0)
D_BLUE		= (  0,   0, 128)
D_MAGENTA	= (128,   0, 128)
D_GREEN		= (  0, 128,   0)
D_YELLOW	= (128, 128,   0)

COLOR_PLAYER = (
BLUE, GREEN, YELLOW, MAGENTA,
D_BLUE, D_GREEN, D_YELLOW, D_MAGENTA
)

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
					"· L'objectif du jeu est d'éliminer les autres joueurs en",
					"capturant tout leurs pions."),
"CREDITS"		: ("Crédit"),
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

LANG_EN = {
"RULES"			: ("Rules"),
"CREDITS"		: ("Credits"),
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

DEFAULT = {
"HEIGHT"	: 720,
"WIDTH"		: 1280,
"LANG"		: LANG_FR
}
