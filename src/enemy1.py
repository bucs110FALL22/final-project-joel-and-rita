import pygame

bullet_image = pygame.image.load('assets/Sprites/Enemies/bullet/bullet.png')

#this creates the bullets that fly acroos the screen using the moving method
class Enemy1(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.x = 0
		self.y = 0
		self.image = pygame.Surface((16,5))
		self.rect = self.image.get_rect(topleft = [x,y])
		self.position = pygame.math.Vector2(x, y)
		self.speed = 5
		self.gravity = float(0.7)
		self.is_moving = True

	def moving(self):
		self.rect.x = self.position.x
		self.position.x -= self.speed
		if self.position.x <= -2000:
			self.position.x = 2000


	def update(self, surface):
		self.moving()
		#print('('+ str(self.rect.x)+ ',' + str(self.rect.y) + ')')
		surface.blit(bullet_image,self.rect)


