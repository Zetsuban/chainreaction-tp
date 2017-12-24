from chainReactionGUI import *

button_function = {
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

class button_c(pygame.sprite.Sprite):

	def __init__(self, text, color, size, function, x, y, pos_type = "center"):

		super().__init__()

		self.color = color
		self.function = function
		self.overed = False
		self.text = text

		self.font = pygame.font.SysFont(None, size)
		self.image = self.font.render(text, True, color)
		self.rect = self.image.get_rect()

		if pos_type == "center":
			self.rect.centerx = x
			self.rect.centery = y
		elif pos_type == "top_left":
			self.rect.left	= x
			self.rect.top	= y

	def update(self, mouse_pos, click = False):
		if self.rect.collidepoint(mouse_pos) and not self.overed:
			self.overed = True
			self.over_in()
		elif not self.rect.collidepoint(mouse_pos) and self.overed:
			self.overed = False
			self.over_out()
		if click and self.rect.collidepoint(mouse_pos):
			button_function[self.function]()

	def over_in(self):
		self.image = self.font.render(self.text, True, MARROON)

	def over_out(self):
		self.image = self.font.render(self.text, True, self.color)
