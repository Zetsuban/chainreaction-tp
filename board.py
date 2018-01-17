import pygame
import constants as c

class board_c(pygame.sprite.Sprite):

	def __init__(self, world, save, size, nb_player):

		super().__init__()

		self.board			= save
		self.size			= size
		self.nb_player		= nb_player
		self.current_player	= 1
		self.turn			= 1

		self.image 			= pygame.Surface((	world.options["HEIGHT"],
												world.options["HEIGHT"]))
		self.rect			= self.image.get_rect()
		self.rect.centerx	= world.options["WIDTH"]  / 2
		self.rect.centery	= world.options["HEIGHT"] / 2

		# define if a chain reaction is producing
		self.in_anim		= False
		self.anim_tick		= 0

        # list of tuple of futur changes in anim
        # a list of all futur state in an anim
        # a state contains a list of all box chaged
        # box = ((posx, posy), player, nb_pawn)
		self.change_list	= 0

		# composed in such a way :
        # self.boxes[x][y] = [pygame.Rect, overed bool]
        # associated with self.board[x][y]
		self.boxes		= [[[0, 0] for i in range(0, size[1])]
							for j in range(0, size[0])]
		boxes_size		= world.options["HEIGHT"]\
						/ (size[0] if size[0] >= size[1] else size[1])
		init_pos_x		= (world.options["HEIGHT"] - boxes_size * size[0]) / 2
		init_pos_y		= (world.options["HEIGHT"] - boxes_size * size[1]) / 2
		for i in range(0, size[0]):		# go through rows
			for j in range(0, size[1]):	# go through cols
				self.boxes[i][j] = [pygame.Rect((	init_pos_y + j * boxes_size,
													init_pos_x + i * boxes_size)
													, (boxes_size, boxes_size)),
									 False]

		self.draw(world)

	def update(self, world):

		mouse_pos	= pygame.mouse.get_pos()
		changed		= False

		for i in self.boxes:
			for j in i:
				j[0].left += (world.options["WIDTH"] - world.options["HEIGHT"]) / 2
				if j[0].collidepoint(mouse_pos) and not j[1]:
					j[1] = True
					changed = True
				if j[1] and not j[0].collidepoint(mouse_pos):
					j[1] = False
					changed = True
				if j[1] and world.click:
					self.turn += 1
					self.current_player = self.current_player % 8 + 1
					changed = True
                    # check if possible move
                    # set changed to True
                    # add pawn
                    # if chain reac set in_anim to True
                    # get change list
				j[0].left -= (world.options["WIDTH"] - world.options["HEIGHT"]) / 2

		# if self.in_anim:
		# 	self.anim_tick += 1

		if changed or self.in_anim:
			self.draw(world)



	def draw(self, world):

		"""if in_anim and anim_tick % 30					\
		update board										\
		blit each box in self.boxes to self.image			\
		draw WHITE lignes (1px width) over self.image		\
		if self.change_list empty							\
		self.anim = False & self.turn += 1"""
		for i in self.boxes :
			for j in i:
				box_img = pygame.Surface((j[0].width, j[0].height))
				box_img.fill(c.D_GRAY if j[1] else c.M_GRAY)
				self.image.blit(box_img, j[0])
				if j[1]:
					pygame.draw.aaline(self.image, c.RED,
									j[0].topleft,
									j[0].bottomright, 3)
					pygame.draw.aaline(self.image, c.RED,
									j[0].topright,
									j[0].bottomleft, 3)

        # draw vertical sides of the boxes
		for i in range(0, self.size[1]):
			pygame.draw.line(self.image,
							c.COLOR_PLAYER[self.current_player - 1],
							self.boxes[0][i][0].topleft,
							self.boxes[self.size[0] - 1][i][0].bottomleft, 5)
		pygame.draw.line(self.image, c.COLOR_PLAYER[self.current_player - 1],
			self.boxes[0][self.size[1] - 1][0].topright,
			self.boxes[self.size[0] - 1][self.size[1] - 1][0].bottomright, 5)

        # draw horizontal sides of the boxes
		for i in range(0, self.size[0]):
			pygame.draw.line(self.image,
							c.COLOR_PLAYER[self.current_player - 1],
							self.boxes[i][0][0].topleft,
							self.boxes[i][self.size[1] - 1][0].topright, 5)
		pygame.draw.line(self.image, c.COLOR_PLAYER[self.current_player - 1],
			self.boxes[self.size[0] - 1][0][0].bottomleft,
			self.boxes[self.size[0] - 1][self.size[1] - 1][0].bottomright, 5)
