import pygame
from src.Level import Level
from src.playbutton import Button

gameWidth = 640
gameHeight = 360
backgroundcolor = (0,0,0)
gamestart = True

maxspeed = 3
midspeed = 2
towerspeed = 2
slowspeed = 1
maxboundaries = 1280

#Initializing pygame and screen
pygame.init()
gamescreen = pygame.display.set_mode((gameWidth,gameHeight))
clock = pygame.time.Clock()

#Load Music
mainmusic = pygame.mixer.music.load("mainmenutheme.mp3")
pygame.mixer.music.play(-1)
#Loads Images
titlesprite = pygame.image.load('assets/Sprites/TitleScreen/TitleScreen.png')
titlesprite_rect = titlesprite.get_rect(center = [320,100])

cloudfront = pygame.image.load('assets/Sprites/TitleScreen/cloud1.png')
cloudfront_rect = cloudfront.get_rect(center = [0,334])
cloudfront2 = pygame.image.load('assets/Sprites/TitleScreen/cloud1.png')
cloudfront_rect2 = cloudfront2.get_rect(center = [1280,334])

cloudmid = pygame.image.load('assets/Sprites/TitleScreen/cloud2.png')
cloudmid_rect = cloudfront.get_rect(center = [0,314])
cloudmid2 = pygame.image.load('assets/Sprites/TitleScreen/cloud2.png')
cloudmid_rect2 = cloudfront2.get_rect(center = [1280,314])

cloudback = pygame.image.load('assets/Sprites/TitleScreen/cloud3.png')
cloudback_rect = cloudfront.get_rect(center = [0,294])
cloudback2 = pygame.image.load('assets/Sprites/TitleScreen/cloud3.png')
cloudback_rect2 = cloudfront2.get_rect(center = [1280,294])

tower = pygame.image.load('assets/Sprites/TitleScreen/tower.png')
tower_rect = tower.get_rect(center = [310,180])

topclouds = pygame.image.load('assets/Sprites/TitleScreen/topclouds.png')
topclouds_rect = tower.get_rect(center = [640,180])
topclouds2 = pygame.image.load('assets/Sprites/TitleScreen/topclouds.png')
topclouds_rect2 = tower.get_rect(center = [1280,180])
play = pygame.image.load('assets/Sprites/TitleScreen/Playbutton.png').convert_alpha()


play_button = Button(275, 250, play)

Level = Level()
		

class MainMenu:
	def __init__(self):
		pass

	def play(self):
		game_state = 0
		while gamestart == True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
			#display images
			gamescreen.fill(backgroundcolor)
			if game_state == 0:
				gamescreen.blit(cloudback,cloudback_rect)
				if cloudback_rect.x > -maxboundaries:
					cloudback_rect.x -= slowspeed
				elif cloudback_rect.x <= -maxboundaries:
					cloudback_rect.x = maxboundaries

				gamescreen.blit(cloudback2,cloudback_rect2)
				if cloudback_rect2.x > -maxboundaries:
					cloudback_rect2.x -= slowspeed
				elif cloudback_rect2.x <= -maxboundaries:
					cloudback_rect2.x = maxboundaries

				gamescreen.blit(cloudmid,cloudmid_rect)
				if cloudmid_rect.x > -maxboundaries:
					cloudmid_rect.x -= midspeed
				elif cloudmid_rect.x <= -maxboundaries:
					cloudmid_rect.x = maxboundaries

				gamescreen.blit(cloudmid2,cloudmid_rect2)
				if cloudmid_rect2.x > -maxboundaries:
					cloudmid_rect2.x -= midspeed
				elif cloudmid_rect2.x <= -maxboundaries:
					cloudmid_rect2.x = maxboundaries

				gamescreen.blit(tower,tower_rect)
				if tower_rect.x > -(maxboundaries/2):
					tower_rect.x -= towerspeed
				elif tower_rect.x <= -(maxboundaries/2):
					tower_rect.x = (maxboundaries/2)

				gamescreen.blit(cloudfront,cloudfront_rect)
				if cloudfront_rect.x > -maxboundaries:
					cloudfront_rect.x -= maxspeed
				elif cloudfront_rect.x <= -maxboundaries:
					cloudfront_rect.x = maxboundaries

				gamescreen.blit(cloudfront2,cloudfront_rect2)
				if cloudfront_rect2.x > -maxboundaries:
					cloudfront_rect2.x -= maxspeed
				elif cloudfront_rect2.x <= -maxboundaries:
					cloudfront_rect2.x = maxboundaries

				gamescreen.blit(topclouds,topclouds_rect)
				if topclouds_rect.x > -(maxboundaries/2):
					topclouds_rect.x -= slowspeed
				elif topclouds_rect.x <= -(maxboundaries/2):
					topclouds_rect.x = (maxboundaries/2)

				gamescreen.blit(topclouds2,topclouds_rect2)
				if topclouds_rect2.x > -(maxboundaries/2):
					topclouds_rect2.x -= slowspeed
				elif topclouds_rect2.x <= -(maxboundaries/2):
					topclouds_rect2.x = (maxboundaries/2)

				gamescreen.blit(titlesprite,titlesprite_rect)

				if play_button.draw(gamescreen):
					print("go to level")
					pygame.mixer.music.stop()
					game_state = 1
				#update screen
			if game_state == 1:
				Level.main(gamescreen)

			pygame.display.flip()
			clock.tick(60)


