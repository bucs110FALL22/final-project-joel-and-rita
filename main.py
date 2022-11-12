import pygame
import random
from src import player
from src import enemy
from src import coin

def main():
  player1 = player.Player()
  pygame.init()
  window = pygame.display.set_mode()
  background = pygame.Surface(pygame.display.get_window_size())
  bgcolor = (0,0,0)
  background.fill(bgcolor)
  enemies = pygame.sprite.Group()
  coins = coin.Coin()

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        exit()
      if event.key == pygame.K_RIGHT:
        player.move("D")

    all_sprites = pygame.sprite.Group(tuple(enemies) + (player, ))

    all_sprites.draw(window)
    pygame.display.flip()
  
    #Create an instance on your controller object
    #Call your mainloop

    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######


# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()

#test

