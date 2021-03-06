import pygame
from pygame.locals import *
import button_function as bf
from constants import *

class game_c():


	def __init__(self, options, save = None):

		self.options	= options
		self.screen		= pygame.display.set_mode((	options["WIDTH"],
													options["HEIGHT"]))
		self.clock		= pygame.time.Clock()
		self.click		= False
		self.running	= True
		self.save		= save
		self.winner		= None

		# self.game_set = [nb_player, nb_row, nb_col]
		self.game_set	= [2, 4, 4]
		self.board		= None
		self.all_object	= None
		self.background = pygame.Surface(self.screen.get_size())
		self.background.fill(BLACK)

		# Save Variables
		self.player		= None
		self.nbPlayer 	= None
		self.row		= None
		self.col		= None
		self.solo		= None
		self.turn		= None


	def event_loop(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				self.exit()
			if event.type == MOUSEBUTTONUP:
				self.click = True


	def world_loop(self):
		bf.main_menu(self)
		if self.save:
			# self.player = int(self.save[0])
			# self.nbPlayer = int(len(self.save[1]))
			# self.row = int(self.save[2])
			# self.col = int(self.save[3])
			# self.turn = int(self.save[5])
			# self.board = self.save[6].split()
			# for i in range(len(self.board)):
			# 	self.board[i] = self.board[i].split(",")
             # Assign saved vlues to continued game
			pass
		while self.running:
			self.screen.blit(self.background, (0, 0))
			self.event_loop()
			self.all_object.update(self)
			self.all_object.draw(self.screen)
			self.click = False
			pygame.display.flip()
			self.clock.tick(60)

	def exit(self):
		self.running = False
