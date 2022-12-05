import pygame

from src.Player1 import Player1

player1 = Player1()
#This class sets the lives for the player
class Lives(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.sprites = []
		self.sprites.append(pygame.image.load('assets/Sprites/LevelScreen/PlayerIcondeath.png'))
		self.sprites.append(pygame.image.load('assets/Sprites/LevelScreen/PlayerIcon.png'))
		self.sprites.append(pygame.image.load('assets/Sprites/LevelScreen/PlayerIcon2.png'))
		self.sprites.append(pygame.image.load('assets/Sprites/LevelScreen/PlayerIcon3.png'))
		self.current_sprite = 3
		self.count = 1
		self.image = self.sprites[self.current_sprite]
		self.rect = self.image.get_rect(topleft = [16,16])

	def livesDecrease(self):
		self.current_sprite -= (1 * self.count)
		self.count = 0
		self.image = self.sprites[self.current_sprite]


	def update(self, surface):
		surface.blit(self.image,self.rect)
#This class sets the score for the player
class Score(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.sprites = []
		self.sprites.append(pygame.image.load('assets/Sprites/LevelScreen/Score0.png'))
		self.sprites.append(pygame.image.load('assets/Sprites/LevelScreen/Score1.png'))
		self.sprites.append(pygame.image.load('assets/Sprites/LevelScreen/Score2.png'))
		self.sprites.append(pygame.image.load('assets/Sprites/LevelScreen/Score3.png'))
		self.sprites.append(pygame.image.load('assets/Sprites/LevelScreen/Score4.png'))
		self.sprites.append(pygame.image.load('assets/Sprites/LevelScreen/Score5.png'))
		self.sprites.append(pygame.image.load('assets/Sprites/LevelScreen/Score6.png'))
		self.sprites.append(pygame.image.load('assets/Sprites/LevelScreen/Score7.png'))
		self.sprites.append(pygame.image.load('assets/Sprites/LevelScreen/Score8.png'))
		self.sprites.append(pygame.image.load('assets/Sprites/LevelScreen/Score9.png'))
		self.sprites.append(pygame.image.load('assets/Sprites/LevelScreen/Score10.png'))
		self.current_sprite = 0
		self.count = 1
		self.image = self.sprites[self.current_sprite]
		self.rect = self.image.get_rect(topleft = [16,48])

	def score_increase(self):
		self.current_sprite += self.count
		if self.current_sprite >= len(self.sprites):
			self.current_sprite = 10
		self.image = self.sprites[self.current_sprite]

	def update(self, surface):
		surface.blit(self.image,self.rect)











