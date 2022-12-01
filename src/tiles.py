import pygame

class Tiles():
	def __init__(self, x, y):
		self.rect = pygame.Rect(x,y,640,60)
		self.x = int(x)
		self.y = int(y)
		self.color = (155,155,155)

	def display(self, surface):
		pygame.draw.rect(surface,self.color,self.rect)
