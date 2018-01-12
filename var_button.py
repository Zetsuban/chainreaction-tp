import pygame
from constants		import *

class var_button_c(pygame.sprite.Sprite):

	def __init__(self, color, size, x, y, var, var_type):

		super().__init__()

		self.font	= pygame.font.SysFont(None, size)
		text_height	= self.font.get_height()
		self.var	= var
		self.color	= color
		self.image	= self.font.render("< " + str(self.var) + " >",
										True, self.color)

		self.minus_box		= self.font.render("<", True, color).get_rect()
		self.plus_box		= self.font.render(">", True, color).get_rect()
		self.minus_overed	= False
		self.plus_overed	= False
		self.var_type		= var_type

		self.set_box(x, y)

	def set_box(self, x, y):
		self.rect				= self.image.get_rect()
		self.rect.centerx		= x
		self.rect.centery		= y
		self.minus_box.left		= x - (self.rect.width / 2) +\
								(self.minus_box.width / 2)
		self.minus_box.centery	= y
		self.plus_box.left		= x + (self.rect.width / 2) -\
								(self.plus_box.width / 2)
		self.plus_box.centery	= y

	def update(self, world):
		mouse_pos = pygame.mouse.get_pos()

		if self.minus_box.collidepoint(mouse_pos) and not self.minus_overed:
			self.minus_overed = True
			self.over_in("minus")
		elif self.plus_box.collidepoint(mouse_pos) and not self.plus_overed:
			self.plus_overed = True
			self.over_in("plus")
		elif not self.minus_box.collidepoint(mouse_pos) and self.minus_overed:
			self.minus_overed = False
			self.over_out()
		elif not self.plus_box.collidepoint(mouse_pos) and self.plus_overed:
			self.plus_overed = False
			self.over_out()

		if world.click and self.minus_overed == True:
			if self.var > GAME_SETTINGS_LIMITE[self.var_type][0]:
				self.var -= 1
				self.over_in("minus")
		elif world.click and self.plus_overed == True:
			if self.var < GAME_SETTINGS_LIMITE[self.var_type][1]:
				self.var += 1
				self.over_in("plus")
				self.set_box(self.rect.centerx, self.rect.centery)

	def over_in(self, side):
		over_color = (	self.color[0] - 100 if self.color[0] - 100 >= 0 else 0 ,
						self.color[1] - 100 if self.color[1] - 100 >= 0 else 0 ,
						self.color[2] - 100 if self.color[2] - 100 >= 0 else 0 )
		if side == "minus":
			plus_img	= self.font.render(str(self.var)  + " >",
										True, self.color)
			minus_img	= self.font.render("< ", True, over_color)
		elif side == "plus":
			plus_img	= self.font.render(" >", True, over_color)
			minus_img	= self.font.render("< " + str(self.var),
											True, self.color)

		self.image.fill(BLACK)
		self.image.blit(minus_img, (0, 0))
		self.image.blit(plus_img, (minus_img.get_width(), 0))

	def over_out(self):
		self.image	= self.font.render("< " + str(self.var) + " >",
										True, self.color)
