import pygame

class Player(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__(self)
    self.x = 0
    self.y = 0
    self.health = 100
    self.image = pygame.image.load("assets/Marioidle1.png")
    self.rect = self.image.get_rect()
    self.walkspeed = 5

  def move_right(self):
    self.rect.x += self.walkspeed

  def move_left(self):
    self.rect.x -= self.walkspeed
    
    