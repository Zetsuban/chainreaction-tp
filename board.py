import pygame
from algorithms			import *
import constants		as c
import button_function	as bf

class board_c(pygame.sprite.Sprite):

	def __init__(self, world, save, size, nb_player):

		super().__init__()

		self.board				= save
		self.size				= size
		self.nb_player			= nb_player if nb_player > 1 else 2
		self.solo				= True if nb_player == 1 else False
		self.current_player		= 1
		self.in_game_players	= [i for i in range(1, self.nb_player + 1)]
		self.turn				= 1
		self.winner				= 0

		self.image 				= pygame.Surface((	world.options["HEIGHT"],
												world.options["HEIGHT"]))
		self.rect				= self.image.get_rect()
		self.rect.centerx		= world.options["WIDTH"]  / 2
		self.rect.centery		= world.options["HEIGHT"] / 2

		# composed in such a way :
		# self.boxes[x][y] = [pygame.Rect, overed bool]
		# associated with self.board[x][y]
		self.boxes	= [[[0, 0] for i in range(0, size[1])]
								for j in range(0, size[0])]
		boxes_size	= world.options["HEIGHT"]\
					/ (size[0] if size[0] >= size[1] else size[1])
		init_pos_x	= (world.options["HEIGHT"] - boxes_size * size[0]) / 2
		init_pos_y	= (world.options["HEIGHT"] - boxes_size * size[1]) / 2
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

		if not self.solo or (self.current_player == 1 and self.solo):
			x = 0
			for i in self.boxes:
				y = 0
				for j in i:
					j[0].left += (world.options["WIDTH"] \
									- world.options["HEIGHT"]) / 2
					if j[0].collidepoint(mouse_pos) and not j[1]:
						j[1] = True
						changed = True
					if j[1] and not j[0].collidepoint(mouse_pos):
						j[1] = False
						changed = True
					if j[1] and world.click and \
							(int(self.board[x][y][1]) == self.current_player \
							or int(self.board[x][y][1]) == 0):
						changed = True
						self.board_update(x, y, world)
					j[0].left -= (world.options["WIDTH"] \
									- world.options["HEIGHT"]) / 2
					y += 1
				x += 1
		elif self.solo:
			x, y = ia(self.board, self.size[0], self.size[1],
						self.current_player)
			self.board_update(x, y, world)
			changed = True

		if changed:
			self.draw(world)

<<<<<<< HEAD
	def board_update(self, x, y, world):
=======
		world.player	= self.current_player
		world.nbPlayer 	= self.nb_player
		world.row		= self.size[0]
		world.col		= self.size[1]
		world.solo		= self.solo
		world.turn		= self.turn

	def board_update(self, x, y):
>>>>>>> 508bfc45249a76d19ef06a0a6251356718440282

		self.board[x][y] =	str(int(self.board[x][y][0]) + 1) + \
							str(self.current_player)
		recursive_put(self.board, self.size[1], self.size[0], y, x,
				self.current_player, self.in_game_players)


		if win(self.board, self.size[1], self.size[0],
				self.current_player, self.nb_player, self.turn,
				self.in_game_players):
			world.winner = self.in_game_players[0]
			world.save = None
			bf.end_game_screen(world)

		self.turn += 1
		self.current_player = self.current_player % self.nb_player + 1

		world.player	= self.current_player
		world.nbPlayer 	= self.in_game_players
		world.row		= len(self.board)
		world.col		= len(self.board[0])
		world.solo		= self.solo
		world.turn		= self.turn


	def draw(self, world):

		x = 0
		for i in self.boxes:
			y = 0
			for j in i:
				box_img = pygame.Surface((j[0].width, j[0].height))
				box_img.fill(c.M_GRAY if j[1] else c.D_GRAY)
				if int(self.board[x][y][0]) == 1:
					pygame.draw.circle(	box_img,
						c.COLOR_PLAYER[int(self.board[x][y][1]) - 1],
						(int(j[0].width / 2), int(j[0].width / 2)),
						int(j[0].width / 14))
				elif int(self.board[x][y][0]) == 2:
					pygame.draw.circle(	box_img,
						c.COLOR_PLAYER[int(self.board[x][y][1]) - 1],
						(int(j[0].width / 4.3), int(j[0].width / 4.3)),
						int(j[0].width / 14))
					pygame.draw.circle(	box_img,
						c.COLOR_PLAYER[int(self.board[x][y][1]) - 1],
						(int(j[0].width - j[0].width / 4.3),
						int(j[0].width - j[0].width / 4.3)),
						int(j[0].width / 14))
				elif int(self.board[x][y][0]) == 3:
					pygame.draw.circle(	box_img,
						c.COLOR_PLAYER[int(self.board[x][y][1]) - 1],
						(int(j[0].width / 4.3), int(j[0].width / 4.3)),
						int(j[0].width / 14))
					pygame.draw.circle(	box_img,
						c.COLOR_PLAYER[int(self.board[x][y][1]) - 1],
						(int(j[0].width / 2), int(j[0].width / 2)),
						int(j[0].width / 14))
					pygame.draw.circle(	box_img,
						c.COLOR_PLAYER[int(self.board[x][y][1]) - 1],
						(int(j[0].width - j[0].width / 4.3),
						int(j[0].width - j[0].width / 4.3)),
						int(j[0].width / 14))
				elif int(self.board[x][y][0]) == 4:
					pygame.draw.circle(	box_img,
						c.COLOR_PLAYER[int(self.board[x][y][1]) - 1],
						(int(j[0].width / 4.3), int(j[0].width / 4.3)),
						int(j[0].width / 14))
					pygame.draw.circle(	box_img,
						c.COLOR_PLAYER[int(self.board[x][y][1]) - 1],
						(int(j[0].width - j[0].width / 4.3),
						int(j[0].width - j[0].width / 4.3)),
						int(j[0].width / 14))
					pygame.draw.circle(	box_img,
						c.COLOR_PLAYER[int(self.board[x][y][1]) - 1],
						(int(j[0].width - j[0].width / 4.3),
						int(j[0].width / 4.3)),
						int(j[0].width / 14))
					pygame.draw.circle(	box_img,
						c.COLOR_PLAYER[int(self.board[x][y][1]) - 1],
						(int(j[0].width / 4.3),
						int(j[0].width - j[0].width / 4.3)),
						int(j[0].width / 14))
				self.image.blit(box_img, j[0])
				if j[1] and int(self.board[x][y][1]) != self.current_player \
						and int(self.board[x][y][1]) > 0:
					pygame.draw.aaline(self.image, c.RED, j[0].topleft,
									j[0].bottomright, 3)
					pygame.draw.aaline(self.image, c.RED, j[0].topright,
									j[0].bottomleft, 3)
				y += 1
			x += 1

        # draw vertical sides of the boxes
		for i in range(0, self.size[1]):
			pygame.draw.line(self.image,
							c.COLOR_PLAYER[self.current_player - 1],
							self.boxes[0][i][0].topleft,
							self.boxes[self.size[0] - 1][i][0].bottomleft, 3)
		pygame.draw.line(self.image, c.COLOR_PLAYER[self.current_player - 1],
			self.boxes[0][self.size[1] - 1][0].topright,
			self.boxes[self.size[0] - 1][self.size[1] - 1][0].bottomright, 3)

        # draw horizontal sides of the boxes
		for i in range(0, self.size[0]):
			pygame.draw.line(self.image,
							c.COLOR_PLAYER[self.current_player - 1],
							self.boxes[i][0][0].topleft,
							self.boxes[i][self.size[1] - 1][0].topright, 3)
		pygame.draw.line(self.image, c.COLOR_PLAYER[self.current_player - 1],
			self.boxes[self.size[0] - 1][0][0].bottomleft,
			self.boxes[self.size[0] - 1][self.size[1] - 1][0].bottomright, 3)
