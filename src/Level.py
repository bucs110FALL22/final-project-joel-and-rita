import pygame
from src.Player1 import Player1
from src.Player1 import detectfinish
from src.tiles import Tiles
from src.score import Lives
from src.score import Score
from src.muncher import Muncher
from src.coins import Coin
from src.enemy1 import Enemy1
from src.backgroundlevel1 import Background
from src.gameover import GameOver
from src.gameover import LevelComplete


#sets up all the class that will be use for the level
over = GameOver()
won = LevelComplete()
playerover = detectfinish()

player1 = Player1()
ground0 = Tiles(-384,56,384,304)
ground1 = Tiles(0,312, 160,48)
ground2 = Tiles(176,248,32,16)
ground3 = Tiles(224,184, 128,176)
ground4 = Tiles(480,248,32,16)
ground5 = Tiles(544,184,32,16)
ground6 = Tiles(480,120,32,16)
ground7 = Tiles(400,300,32,16)

ground8 = Tiles(224, 176, 16, 8)
ground9 = Tiles(336, 176, 16, 8)

coin1 = Coin(190,216)
coin2 = Coin(342,144)
coin3 = Coin(416,268)
coin4 = Coin(496,88)

bullet = Enemy1(750,250)
bullet2 = Enemy1(-1400,150)
bullet3 = Enemy1(2000,50)
bullet4 = Enemy1(-100,190)
levelbackground = Background()

muncherx = 300
munchery = 300
muncher1 = Muncher(muncherx,munchery)

LiveCount = Lives()
ScoreCount = Score()

groundgroup = pygame.sprite.Group()
groundgroup.add(ground0)
groundgroup.add(ground1)
groundgroup.add(ground2)
groundgroup.add(ground3)
groundgroup.add(ground4)
groundgroup.add(ground5)
groundgroup.add(ground6)
groundgroup.add(ground7)
groundgroup.add(ground8)
groundgroup.add(ground9)

enemyflygroup = pygame.sprite.Group()
enemyflygroup.add(bullet)
enemyflygroup.add(bullet2)
enemyflygroup.add(bullet3)
enemyflygroup.add(bullet4)

coingroup = pygame.sprite.Group()
coingroup.add(coin1)
coingroup.add(coin2)
coingroup.add(coin3)
coingroup.add(coin4)

enemygroup = pygame.sprite.Group()
enemygroup.add(muncher1)

#Runs the level in this class, calling in methods from different classes
class Level:
	def __init__(self):
		pass

	def game(self):
		self.game_state = 1

	def player_level(self):
		game_state = 1
		#self.player1 = pygame.sprite.GroupSingle()
  #sets collision for player horizontally
	def horizontalCollision(self): 
		player1.rect.x += (player1.position.x * player1.speed)
		for sprite in groundgroup:
			if sprite.rect.colliderect(player1.rect):
				if player1.position.x < 0:
					player1.rect.left = sprite.rect.right
					player1.xcolliding = True
				elif player1.position.x > 0:
					player1.rect.right = sprite.rect.left
					player1.xcolliding = True
			else:
				player1.xcolliding = False		
  #sets collision for player vertically
	def verticalCollision(self):
		player1.apply_gravity()
		for sprite in groundgroup:
			if sprite.rect.colliderect(player1.rect):
				if player1.position.y > 0:
					player1.rect.bottom = sprite.rect.top
					player1.position.y = 0
					player1.is_on_ground = True
				elif player1.position.y < 0:
					player1.rect.top = sprite.rect.bottom
					player1.position.y = 0
  #sets collision for muncher horizontally
	def enemyhorizontalCollision(self): 
		muncher1.rect.x += (muncher1.position.x * muncher1.speed) 
		for sprite in groundgroup:
			if sprite.rect.colliderect(muncher1.rect):
				if muncher1.rect.x < 1 or muncher1.rect.x > 1:
					muncher1.xcolliding = True
					muncher1.speed = muncher1.speed * -1
			else:
				muncher1.xcolliding = False		
  #sets collision for muncher vertically
	def enemyverticalCollision(self):
		muncher1.apply_gravity()
		if muncher1.rect.y >= 370:
			for sprite in enemygroup:
				enemygroup.remove(sprite)
		for sprite in groundgroup:
			if sprite.rect.colliderect(muncher1.rect):
				if muncher1.position.y > 0:
					muncher1.rect.bottom = sprite.rect.top
					muncher1.position.y = 0
					muncher1.is_on_ground = True
				elif player1.position.y < 0:
					muncher1.rect.top = sprite.rect.bottom
					muncher1.position.y = 0
  #detects collision between player and muncher
	def collisionWithmuncherCheck(self):
		for sprite in enemygroup:
			if sprite.rect.colliderect(player1.rect):
				if player1.position.y >= 0 and not player1.position.x < 0 and not player1.position.x > 0 and not player1.position.y < 0:
					player1.rect.bottom = sprite.rect.top
					muncher1.squished()
					if muncher1.is_squished == True:
						enemygroup.remove(sprite)
				elif not player1.position.y >= 0 and player1.position.x < 0 or player1.position.x > 0 or player1.position.y < 0:
					player1.is_hurt = True	
					LiveCount.livesDecrease()
	#detects collision between player and bullet
	def collisionWithBulletCheck(self):
		for sprite in enemyflygroup:
			if sprite.rect.colliderect(player1.rect):
				if player1.position.x < 0 or player1.position.x > 0 or player1.position.y > 0 or player1.position.y < 0:
					player1.is_hurt = True	
					LiveCount.livesDecrease()	
  #detects collision between player and coin, if player touches coin the score goes up by 1
	def collisionWithCoin(self):
		for sprite in coingroup:
			if sprite.rect.colliderect(player1.rect):
				if player1.position.x < 0 or player1.position.x > 0 or player1.position.y > 0 or player1.position.y < 0:
					player1.score += 1
					ScoreCount.score_increase()
					coingroup.remove(sprite)
					#delete coin					
          
  #updates the livecount icone base the players health set to 3
	def live_update(self):
		LiveCount.current_sprite = player1.health
  #updates the score count base on players score
	def score_update(self):
		ScoreCount.current_sprite = player1.score
    
  #detects if player loses
	def gameover(self):
		playerover.lose = True
  #detects if player wins
	def gamewon(self):
		playerover.win = True
  #Runs the level and all the classes called
	def main(self, surface):
		game_state = 1
		if playerover.lose == True:
			game_state = 2
		if playerover.win == True:
			game_state = 3
		if game_state == 1:
			levelbackground.play(surface)
			player1.update(surface)
			groundgroup.draw(surface)	
			LiveCount.update(surface)
			ScoreCount.update(surface)
			coingroup.update(surface)
			coingroup.draw(surface)
			enemygroup.update(surface)
			enemyflygroup.update(surface)
			self.collisionWithCoin()
			self.live_update()
			self.horizontalCollision()
			self.verticalCollision()
			self.enemyhorizontalCollision()
			self.enemyverticalCollision()
			self.collisionWithBulletCheck()
			self.collisionWithmuncherCheck()
      #moves to different screen depending on whether the player won or lose
			if player1.rect.y >= 376 or player1.health == 0:
				self.gameover()
			if player1.score == 4:
				self.gamewon()
		if game_state == 2:
			over.play(surface)
		elif game_state == 3:
			won.play(surface)
