import pygame
from button_function import *
from pygame.locals import *

class game_c():

	def __init__(self, options, save = None):

		self.options	= options
		self.screen		= pygame.display.set_mode((	options["WIDTH"],
													options["HEIGHT"]))
		self.click		= False
		self.running	= True
		self.board		= save
		self.all_object	= None
		main_menu(self)

	def event_loop(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				self.exit()
			if event.type == MOUSEBUTTONDOWN:
				self.click = True
			if event.type == MOUSEBUTTONUP:
				self.click = False

	def world_loop(self):
		while self.running:
			self.event_loop()
			self.all_object.update(self)
			self.all_object.draw(self.screen)
			pygame.display.flip()

	def exit(self):
		self.running = False
