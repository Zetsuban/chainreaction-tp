import pygame
import button_function
from constants import *

class var_text_c(pygame.sprite.Sprite):

	def __init__(self, var_type, size, color, text, x, y):

		super().__init__()

		self.var_type	= var_type
		self.color		= color
		self.text		= text
		self.var		= 0

		self.font		= pygame.font.SysFont(None, size)
		self.image		= self.font.render(text + str(self.var), True, color)
		self.rect		= self.image.get_rect()
		self.rect.top	= x
		self.rect.left	= y


	def update(self, world):

		for i in world.all_object.sprites():
			if type(i) == VAR_TYPE[self.var_type] and \
					getattr(i, VAR[self.var_type], None) != self.var:
				self.var = getattr(i, VAR[self.var_type], None)
				self.image	= self.font.render(self.text + str(self.var),
												True, self.color)
