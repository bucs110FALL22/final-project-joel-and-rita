import pygame

class Enemy(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__(self)
    self.health = 1
    self.image = pygame.image.load("assets/Goomba_Walk1.png")
    self.rect = self.image.get_rect()
    self.walkspeed = 2

  def move_right(self):
    self.rect.x += self.walkspeed

  def move_left(self):
    self.rect.x -= self.walkspeed
    
    