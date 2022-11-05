import pygame, sys
import random


#Player---
#-------------
platforms = [
  #Starting platform
  pygame.Rect(0,270,640,50),
  #top plat
  pygame.Rect(200,220,50,50)
]

coinw = 12
coinh = 12
coincolor = "yellow"
coins = [
  pygame.Rect(220,200,coinw,coinh),
  pygame.Rect(450,200,coinw,coinh)
]

enemyx = 300
enemyy = 245
enemyw = 25
enemyh = 25
enemycolor = "brown"
enemyfallspeed = 0
enemyaccel = 0.5
enemies = [
  pygame.Rect(enemyx,enemyy,enemyw,enemyh)
]

tilecolor = "darkgreen"
screen_width = 640
screen_height = 320
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
#import your controller


def main():
  #Player 1---
  lives = 3
  lifex = 100
  lifey = 5
  knockback = 0
  p1x = 0
  p1y = 0
  p1w = 25
  p1h = 50
  p1jump = 10
  p1speed = 2
  p1fallspeed = 0
  p1accel = 0.5
  p1color = pygame.Color(236, 233, 132)
  player1 = pygame.Rect(p1x,p1y,p1w,p1h)
  score = 0
  #---
  
  pygame.init()
  gamestate = "playing"
  fontcolor = "white"
  font = pygame.font.Font(pygame.font.get_default_font(), 24)
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    screen.fill("black")
    #Player1 controls
    updatedp1x = p1x
    updatedp1y = p1y
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
      updatedp1x -= p1speed
    if keys[pygame.K_d]:
      updatedp1x += p1speed
    if keys[pygame.K_k] and p1onground:
      p1fallspeed = -p1jump

    updatedplayer1 = pygame.Rect(updatedp1x,p1y,p1w,p1h)
    x_collision = False

    for p in platforms:
      if p.colliderect(updatedplayer1):
        x_collision = True
        break
    
    if x_collision == False:
      p1x = updatedp1x

    #gravity
    p1fallspeed += p1accel
    updatedp1y += p1fallspeed
    
    updatedplayer1 = pygame.Rect(p1x,updatedp1y,p1w,p1h)
    y_collision = False
    p1onground = False
    
    for p in platforms:
      if p.colliderect(updatedplayer1):
        y_collision = True
        p1fallspeed = 0
        if p[1] >= updatedp1y:
          p1y = p[1] - p1h
          p1onground = True
        break

    if y_collision == False:
      p1y = updatedp1y
    
    player1 = pygame.Rect(p1x,p1y,p1w,p1h)
    for c in coins: 
      if c.colliderect(player1):
        coins.remove(c)
        score += 1
      if score >= 2:
        gamestate = "win"
    #print(score)

    for e in enemies: 
      if e.colliderect(player1) and p1x <= enemyx:
        p1x -= (knockback + 30)
        p1y -= (knockback + 30)
        lives -= 1
      if e.colliderect(player1) and p1x > enemyx:
        p1x += (knockback + 30)
        p1y += (knockback + 30)
        lives -= 1
      if lives <= 0:
        gamestate = "lose"
    
    pygame.draw.rect(screen,p1color,player1)
    #----

    #Platform---
    for p in platforms:
      pygame.draw.rect(screen,tilecolor,p)
    #---
    for c in coins:
      pygame.draw.rect(screen,coincolor,c)

    for e in enemies:
      pygame.draw.rect(screen,enemycolor,e)

    
  

    #print("coordinates:(",p1x, ",",p1y,")")
    scoretext = font.render("Score:" + str(score),True,fontcolor,"black")
    scoretextrectangle = scoretext.get_rect()
    screen.blit(scoretext, scoretextrectangle)
    for l in range(lives):
      lifeicon = pygame.Rect((lifex + (l*25)),lifey,15,15)
      pygame.draw.rect(screen,p1color,lifeicon)

    if gamestate == "win":
      pygame.quit()
      sys.exit()
    if gamestate == "lose":
      pygame.quit()
      sys.exit()
      
    pygame.display.update()
    clock.tick(60)
    #Create an instance on your controller object
    #Call your mainloop

    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######


# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()

#test

