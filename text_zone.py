import pygame

class text_zone_c(pygame.sprite.Sprite):

	def __init__(self, text, color, size, x, y, align = "left",
					pos_type = "center"):

		super().__init__()

		self.font = pygame.font.SysFont(None, size)

		img_width = 0
		txt_width = 0

		for i in text:
			if len(i) > txt_width:
				txt_width = len(i)
				img_width = self.font.render(i, True, color).get_width()

		self.image = pygame.Surface((img_width,
			self.font.get_height() * len(text)))


		if align == "left":
			for i in range(0, len(text)):
				self.image.blit(self.font.render(text[i], True, color),
									(0, i * (size / 1.5 + 1))             )
		elif align == "center":
			for i in range(0, len(text)):
					line_img = self.font.render(text[i], True, color)
					self.image.blit(line_img,
					((img_width - line_img.get_width()) / 2, i * (size / 1.5 + 1)))

		self.rect = self.image.get_rect()
		if pos_type == "center":
			self.rect.centerx = x
			self.rect.centery = y
		elif pos_type == "top_left":
			self.rect.left	= x
			self.rect.top	= y

	def update(self, world):
		pass
