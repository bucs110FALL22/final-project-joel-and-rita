import pygame
from src.Level import Level
from src.playbutton import Button

#Sets the gamescreen dimensions and color
gameWidth = 640
gameHeight = 360
backgroundcolor = (0,0,0)
gamestart = True

#Speed for the images moving through the titlescreen
maxspeed = 3
midspeed = 2
towerspeed = 2
slowspeed = 1
maxboundaries = 1280

#Initializing pygame and screen
pygame.init()
gamescreen = pygame.display.set_mode((gameWidth,gameHeight))
clock = pygame.time.Clock()

#Loads Images and setting the posisitions
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

#sets the game state to 0 to play the game and the play/level button class
game_state = 0
play_button = Button(275, 250, play)

Level = Level()

#runs the mainmenu
class MainMenu:
	def __init__(self):
		pass
#Players the menu once game_state = 0 and moves each image until reaching max boundaries
#After the images touches the maxboundaries, it is sent back to its starting position to move again
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
        #Displays the play button
				if play_button.draw(gamescreen):
					game_state = 1
				#if game_state = 1 the game moves onto the level
			if game_state == 1:
				Level.main(gamescreen)
      #update screen
			pygame.display.flip()
			clock.tick(60)


