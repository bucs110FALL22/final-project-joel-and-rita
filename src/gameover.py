import pygame

from src.quitbutton import Button
#Loads Images
gameover = pygame.image.load('assets/Sprites/GameOverScreen/GameOver.png')
gameover_rect = gameover.get_rect(center = [320,100])

levelcomplete = pygame.image.load('assets/Sprites/GameOverScreen/levelcomplete.png')
levelcomplete_rect = levelcomplete.get_rect(center = [320,100])

quit = pygame.image.load('assets/Sprites/GameOverScreen/quit.png')
quit_button = Button(275, 250, quit)
#This class works exactly like the main menu class
class GameOver:
	def __init__(self):
		pass

	def play(self, surface):
		game_state = 2
		if game_state == 2:
			surface.blit(gameover,gameover_rect)
			if quit_button.draw(surface):
				game_state = 4
				#update screen
			if game_state == 4:
				pygame.quit()

class LevelComplete:
	def __init__(self):
		pass

	def play(self,surface):
		game_state = 3
		if game_state == 3:
			surface.blit(levelcomplete,levelcomplete_rect)
			if quit_button.draw(surface):
				game_state = 4
				#update screen
			if game_state == 4:
				pygame.quit()





