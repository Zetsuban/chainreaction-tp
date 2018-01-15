import pygame
import button_function

class var_text_c(pygame.sprite.Sprite):

    # text format :
    # %% = %
    # %c = counter
	def __init__(self, number, size, color, text, x, y):

		super().__init__()

		self.number	= number
		self.color	= color
		self.text	= text

		self.font		= pygame.font.SysFont(None, size)
		self.image		= self.font.render(text + str(self.number), True, color)
		self.rect		= self.image.get_rect()
		self.rect.top	= x
		self.rect.left	= y


	def update(self, world):

		for i in world.all_object.sprites():
			if type(i) == button_function.dummy_c and i.turn != self.number:
				self.number = i.turn
				self.image	= self.font.render(self.text + str(self.number),
												True, self.color)
