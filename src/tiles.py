import pygame

ground_image = pygame.image.load('assets/Sprites/Tiles/ground.png')

color = (100,100,100)
class Tiles(pygame.sprite.Sprite):

	def __init__(self, x, y, w, h):
		super().__init__()
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((w,h))
		self.image.fill(color)
		self.rect = self.image.get_rect(topleft = (x,y))
	
		
	def display(self, surface):
		surface.blit(ground_image, self.rect)

	

