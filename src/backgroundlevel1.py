import pygame

maxspeed = 3
midspeed = 2
towerspeed = 2
slowspeed = 1
maxboundaries = 1280

#Loads Images
titlesprite = pygame.image.load('assets/Sprites/TitleScreen/TitleScreen.png')
titlesprite_rect = titlesprite.get_rect(center = [320,100])

cloudfront = pygame.image.load('assets/Sprites/TitleScreen/cloud1.png')
cloudfront_rect = cloudfront.get_rect(center = [0,354])
cloudfront2 = pygame.image.load('assets/Sprites/TitleScreen/cloud1.png')
cloudfront_rect2 = cloudfront2.get_rect(center = [1280,354])

cloudmid = pygame.image.load('assets/Sprites/TitleScreen/cloud2.png')
cloudmid_rect = cloudmid.get_rect(center = [0,334])
cloudmid2 = pygame.image.load('assets/Sprites/TitleScreen/cloud2.png')
cloudmid_rect2 = cloudmid2.get_rect(center = [1280,334])

cloudback = pygame.image.load('assets/Sprites/TitleScreen/cloud3.png')
cloudback_rect = cloudback.get_rect(center = [0,314])
cloudback2 = pygame.image.load('assets/Sprites/TitleScreen/cloud3.png')
cloudback_rect2 = cloudback2.get_rect(center = [1280,314])


topclouds = pygame.image.load('assets/Sprites/TitleScreen/topclouds.png')
topclouds_rect = topclouds.get_rect(center = [640,120])
topclouds2 = pygame.image.load('assets/Sprites/TitleScreen/topclouds.png')
topclouds_rect2 = topclouds2.get_rect(center = [1280,120])

class Background:
	def __init__(self):
		pass

	def play(self, surface):
		surface.blit(cloudback,cloudback_rect)
		if cloudback_rect.x > -maxboundaries:
			cloudback_rect.x -= slowspeed
		elif cloudback_rect.x <= -maxboundaries:
			cloudback_rect.x = maxboundaries

		surface.blit(cloudback2,cloudback_rect2)
		if cloudback_rect2.x > -maxboundaries:
			cloudback_rect2.x -= slowspeed
		elif cloudback_rect2.x <= -maxboundaries:
			cloudback_rect2.x = maxboundaries

		surface.blit(cloudmid,cloudmid_rect)
		if cloudmid_rect.x > -maxboundaries:
			cloudmid_rect.x -= midspeed
		elif cloudmid_rect.x <= -maxboundaries:
			cloudmid_rect.x = maxboundaries

		surface.blit(cloudmid2,cloudmid_rect2)
		if cloudmid_rect2.x > -maxboundaries:
			cloudmid_rect2.x -= midspeed
		elif cloudmid_rect2.x <= -maxboundaries:
			cloudmid_rect2.x = maxboundaries

		surface.blit(cloudfront,cloudfront_rect)
		if cloudfront_rect.x > -maxboundaries:
			cloudfront_rect.x -= maxspeed
		elif cloudfront_rect.x <= -maxboundaries:
			cloudfront_rect.x = maxboundaries

		surface.blit(cloudfront2,cloudfront_rect2)
		if cloudfront_rect2.x > -maxboundaries:
			cloudfront_rect2.x -= maxspeed
		elif cloudfront_rect2.x <= -maxboundaries:
			cloudfront_rect2.x = maxboundaries

		surface.blit(topclouds,topclouds_rect)
		if topclouds_rect.x > -(maxboundaries/2):
			topclouds_rect.x -= slowspeed
		elif topclouds_rect.x <= -(maxboundaries/2):
			topclouds_rect.x = (maxboundaries/2)

		surface.blit(topclouds2,topclouds_rect2)
		if topclouds_rect2.x > -(maxboundaries/2):
			topclouds_rect2.x -= slowspeed
		elif topclouds_rect2.x <= -(maxboundaries/2):
			topclouds_rect2.x = (maxboundaries/2)