import pygame
from src.tiles import Tiles
ground1 = Tiles(0,300)
platforms = [
	ground1
]

class Player():
	def __init__(self, x, y):
		self.rect = pygame.Rect(x,y, 32, 64)
		self.x = int(x)
		self.y = int(y)
		self.color = (255,255,255)
		self.dx = 0
		self.dy = 0
		self.speed = 5
		self.jump = False
		self.right_pressed = False
		self.left_pressed = False
		self.up_pressed = False
		self.down_pressed = False
		self.is_on_ground = False
		self.jump = False
		self.jump_count = 0
		self.gravity = float(0.7)

	def display(self, surface):
		pygame.draw.rect(surface,self.color,self.rect)




	def player_input(self):
		self.dx = 0
		#gravity
		if self.is_on_ground == False:
			self.dy += self.gravity
		if self.is_on_ground == True:
			self.dy = (self.dy * 0)
			self.jump_count = 0

	

		#Moves the player according to the button pressed	
		if self.right_pressed == True and self.left_pressed == False:
			self.dx += self.speed
		if self.right_pressed == False and self.left_pressed == True:
			self.dx += -self.speed
		if self.right_pressed == False and self.left_pressed == False:
			self.dx = self.dx


		if self.is_on_ground == True:
			if self.jump == True and self.jump_count == 0:
				self.jump_count = 1
				self.dy -= 10
				self.is_on_ground = False
				print("jump")

		self.x += self.dx
		self.y += self.dy
		self.rect = pygame.Rect(self.x, self.y, 32, 64)



		




	