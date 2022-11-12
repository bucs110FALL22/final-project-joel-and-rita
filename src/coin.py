import pygame
from src import Player

class Coin(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__(self)
    self.image = pygame.image.load("assets/Marioidle1.png")
    self.rect = self.image.get_rect()

  def collide(self)
  ## placeholder code
    if self.rect.x <= player1.x:
      remove coin
  
    
