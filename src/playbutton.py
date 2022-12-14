import pygame

#Loadsimage
playhovered = pygame.image.load('assets/Sprites/TitleScreen/Playbuttonhovered.png')

#this class sets the variables, then creates a method that displays the button
#within method draw if the user clicks on it the button responds
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
			surface.blit(playhovered,(self.rect.x,self.rect.y))
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				surface.blit(self.image,(self.rect.x,self.rect.y))
				self.clicked = True
				playclicked = True
		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		return playclicked