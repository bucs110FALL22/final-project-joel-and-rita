import pygame
from src.Player import Player
from src.tiles import Tiles


player = Player(0,0)
ground1 = Tiles(0,300)

class Level:
	def __init__(self):
		pass

	def main(self, surface):
		player.display(surface)
		player.player_input()
		ground1.display(surface)
		if player.rect.y >= (ground1.rect.y-60):
			player.is_on_ground = True
		keys = pygame.key.get_pressed()
		if keys[pygame.K_d] and keys[pygame.K_w]:
			player.right_pressed = True
			player.left_pressed = False
			player.jump = True
		elif keys[pygame.K_a] and keys[pygame.K_w]:
			player.right_pressed = False
			player.left_pressed = True
			player.jump = True
		elif keys[pygame.K_d]:
			player.right_pressed = True
			player.left_pressed = False
			player.jump = False
		elif keys[pygame.K_a]:
			player.right_pressed = False
			player.left_pressed = True
			player.jump = False
		elif keys[pygame.K_w]: 
			player.jump = True
		else:
			player.right_pressed = False
			player.left_pressed = False
			player.jump = False

		print('level')