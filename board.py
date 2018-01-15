class board_c(pygame.sprite.Sprite):

	def __init__(self, world, save, size, nb_player):

		super().__init__()

		self.board			= save
		self.size			= size
		self.nb_player		= nb_player

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
		self.change_list = 0

		# composed in such a way :
        # self.boxes[x][y] = [pygame.Rect, overed bool]
        # associated with self.board[x][y]
		self.boxes			= [[0, 0] * size[1]] * size[0]

		boxes_size			= (size[0] if size[0] >= size[1] else size[1])\
								/ world.options["HEIGHT"]
		init_pos_x			= (world.options["HEIGHT"] - boxes_size * size[0])\
								/ 2
		init_pos_y			= (world.options["HEIGHT"] - boxes_size * size[1])\
								/ 2
		for i in range(0, size[0]):		# go through rows
			for j in range(0, size[1]):	# go through cols
				self.boxes[i][j] = [pygame.Rect((	init_pos_y + j * boxes_size,
													init_pos_y + i * boxes_size)
													, (boxes_size, boxes_size)),
									 False]

	def update(self, world):

		mouse_pos = pygame.mouse.get_pos()

		for i in self.boxes:
			for j in i:
				if j[0].collidepoint(mouse_pos) and not j[1]:
					j[1] = True
					changed = True
				if j[1] and not j[0].collidepoint(mouse_pos):
					j[1] = False
					changed = True
				if j[1] and world.click:
                    # check if possible move
                    # set changed to True
                    # add pawn
                    # if chain reac set in_anim to True
                    # get change list

		if self.in_anim:
			self.anim_tick += 1

		if changed or self.in_anim:
			self.draw()



	def draw(self):
        # if in_anim and anim_tick % 30
        # update board
        # blit each box in self.boxes to self.image
        # draw WHITE lignes (1px width) over self.image
		pass
