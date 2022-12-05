import pygame

#Loadsimage
quithovered = pygame.image.load('assets/Sprites/GameOverScreen/quithovered.png')

#This sets the quit button which works the same as the play button
class Button():
	def __init__(self, x, y, image):
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.topleft = (x,y)
		self.clicked = False

	def draw(self, surface):
		playclicked = False
		surface.blit(self.image,(self.rect.x,self.rect.y))
		pos = pygame.mouse.get_pos()
		#detect mouseclick
		if self.rect.collidepoint(pos):
			surface.blit(quithovered,(self.rect.x,self.rect.y))
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				surface.blit(self.image,(self.rect.x,self.rect.y))
				self.clicked = True
				playclicked = True
		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		return playclicked