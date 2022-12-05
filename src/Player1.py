import pygame

#this class sets the players sprite, movement, gravity and variables
#with each method corresponding to each part of the player
class Player1(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.sprites = []
		self.sprites.append(pygame.image.load('assets/Sprites/Player/Player1.png'))
		self.sprites.append(pygame.image.load('assets/Sprites/Player/Player1hurt.png'))
		self.current_sprite = 0
		self.image = pygame.Surface((16,32))
		self.image = self.sprites[self.current_sprite]
		self.rect = self.image.get_rect(topleft = [0,0])
		self.position = pygame.math.Vector2(0, 0)
		self.speed = 2
		self.gravity = float(0.7)
		self.moving = False
		self.jumpheight = -10
		self.is_jumping = False
		self.is_on_ground = False
		self.xcolliding = False
		self.is_ycolliding = False
		self.cameramovedown = False
		self.is_hurt = False
		self.hurtTimer = 30
		self.health = 3
		self.damage = 1
		self.playerover = False
		self.score = 0
		self.bounce = False

	def idle(self):
		self.position.x = 0
		self.position.y = self.position.y

	def moveleft(self):
		self.position.x = -self.speed

	def moveright(self):
		self.position.x = self.speed

	def jump(self):
		if self.is_on_ground == True and self.is_hurt == False:
			self.position.y = self.jumpheight
			self.is_on_ground = False
			self.bounce = False

	def runleftjump(self):
		self.position.x = -self.speed
		if self.is_on_ground == True and self.is_hurt == False:
			self.position.y = self.jumpheight
			self.is_on_ground = False

	def runrightjump(self):
		self.position.x = -self.speed
		if self.is_on_ground == True and self.is_hurt == False:
			self.position.y = self.jumpheight
			self.is_on_ground = False

	def jumpidle(self):
		if self.is_on_ground == True and self.is_hurt == False:
			self.position.y = self.jumpheight
			self.is_on_ground = False

	def apply_gravity(self):
		self.position.y += self.gravity
		self.rect.y += self.position.y
		if self.rect.y != 0:
			self.is_on_ground = False

	def bounce_up(self):
		self.jump()

	def bounce_back(self):
		pass

	def hurt(self):
		if self.health > 0:
			self.health -= (1 * self.damage)
			self.hurtTimer -= 1
		if self.hurtTimer > 0 and self.hurtTimer < 30:
			self.damage = 0
			self.current_sprite = 1
			self.image = self.sprites[self.current_sprite]
		else:
			self.damage = 1
			self.current_sprite = 0
			self.hurtTimer = 30
			self.image = self.sprites[self.current_sprite]
			self.is_hurt = False


	def player_input(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_d] and keys[pygame.K_k] and not keys[pygame.K_a]:
			self.runrightjump()
		elif keys[pygame.K_a] and keys[pygame.K_k] and not keys[pygame.K_d]:
			self.runleftjump()
		elif keys[pygame.K_a] and keys[pygame.K_k] and keys[pygame.K_d]:
			self.jumpidle()
		elif keys[pygame.K_k] and not keys[pygame.K_d] and not keys[pygame.K_a]: 
			self.jump()
		if keys[pygame.K_d] and not keys[pygame.K_a]:
			self.moveright()
		elif keys[pygame.K_a] and not keys[pygame.K_d]:
			self.moveleft()	
		else:
			self.idle()

	def update(self, surface):
		if self.is_hurt == True:
			self.hurt()
		elif self.bounce == True:
			self.bounce_up()
		self.player_input()
		#print('('+ str(self.rect.x)+ ',' + str(self.rect.y) + ')')
		surface.blit(self.image,self.rect)
	
class detectfinish():
	def __init__(self):
		self.over = False
		self.win = False

	def lose(self):
		self.over()

	def win(self):
		self.win()



	
	


			




	