import pygame

#This class sets the muncher variables and methods
class Muncher(pygame.sprite.Sprite):
	def __init__(self,x ,y):
		super().__init__()
		self.sprites = []
		self.sprites.append(pygame.image.load('assets/Sprites/Enemies/munchers/muncher.png'))
		self.sprites.append(pygame.image.load('assets/Sprites/Enemies/munchers/muncherhurt.png'))
		self.current_sprite = 0
		self.x = 0
		self.y = 0
		self.image = pygame.Surface((16,8))
		self.image = self.sprites[self.current_sprite]
		self.rect = self.image.get_rect(topleft = [x,y])
		self.position = pygame.math.Vector2(1, 0)
		self.speed = -1
		self.gravity = float(0.7)
		self.is_on_ground = False
		self.is_xcolliding = False
		self.count = 1
		self.is_squished = False

	def move(self):
		pass
  #Plays the squish animation and apply gravity to it
	def squished(self):
		self.current_sprite += 1
		self.image = self.sprites[self.current_sprite]
		if self.current_sprite == 1:
			self.is_squished = True
  
	def apply_gravity(self):
		self.position.y += self.gravity
		self.rect.y += self.position.y
		if self.rect.y != 0:
			self.is_on_ground = False
	
	def update(self, surface):
		surface.blit(self.image,self.rect)