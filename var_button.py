import pygame
from constants		import *

class var_button_c(pygame.sprite.Sprite):

	def __init__(self, color, size, x, y, var, var_type):

		super().__init__()

		self.font		= pygame.font.SysFont(None, size)
		text_height		= self.font.get_height()
		self.var		= var
		self.color		= color
		self.over_color	= (
						self.color[0] - 100 if self.color[0] - 100 >= 0 else 0 ,
						self.color[1] - 100 if self.color[1] - 100 >= 0 else 0 ,
						self.color[2] - 100 if self.color[2] - 100 >= 0 else 0 )

		self.minus_overed	= False
		self.plus_overed	= False
		self.var_type		= var_type

		self.image 			= pygame.Surface(
			(self.font.render("<", True, color).get_width() * 2 + 50,
			text_height))
		self.rect 				= self.image.get_rect()
		self.rect.centerx		= x
		self.rect.centery		= y
		self.minus_box			= self.font.render("<", True, color).get_rect()
		self.plus_box			= self.font.render(">", True, color).get_rect()
		self.minus_box.topleft	= self.rect.topleft
		self.plus_box.topright	= self.rect.topright
		self.draw()

	def draw(self):
		self.image.fill(BLACK)
		self.image.blit(self.font.render("<", True,
			self.over_color if self.minus_overed else self.color),
			(0, 0))
		self.image.blit(self.font.render(">", True,
			self.over_color if self.plus_overed else self.color),
			(self.rect.width - self.plus_box.width, 0))
		if len(str(self.var)) == 2:
			self.image.blit(self.font.render(str(self.var), True, self.color),
				(self.rect.width / 2 - self.plus_box.width, 0))
		else:
			self.image.blit(self.font.render(str(self.var), True, self.color),
				(self.rect.width / 2 - self.font.render(str(self.var), True, self.color).get_width() / 2, 0))

	def update(self, world):
		mouse_pos	= pygame.mouse.get_pos()
		changed		= False

		if self.minus_box.collidepoint(mouse_pos) and not self.minus_overed:
			self.minus_overed	= True
			changed				= True
		elif self.plus_box.collidepoint(mouse_pos) and not self.plus_overed:
			self.plus_overed	= True
			changed				= True
		elif not self.minus_box.collidepoint(mouse_pos) and self.minus_overed:
			self.minus_overed	= False
			changed				= True
		elif not self.plus_box.collidepoint(mouse_pos) and self.plus_overed:
			self.plus_overed	= False
			changed				= True

		if world.click and self.minus_overed == True:
			if self.var > GAME_SETTINGS_LIMITE[self.var_type][0]:
				self.var			-= 1
				changed				= True
		elif world.click and self.plus_overed == True:
			if self.var < GAME_SETTINGS_LIMITE[self.var_type][1]:
				self.var			+= 1
				changed				= True

		if world.game_set[self.var_type] != self.var:
			world.game_set[self.var_type] = self.var

		if changed:
			self.draw()
