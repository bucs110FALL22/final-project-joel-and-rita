import pygame

color = (255, 100, 98)
surface_color = (167, 255, 100)
width = 500
height = 500

class Tile(pygame.sprite.Sprite):
  def __init__(self,color,height,width):
    super().__init__()
    self.image = pygame.Surface([width,height])
    self.image.fill(surface_color)
    self.image.set_colorkey(color)
    pygame.draw.rect(self.image,color,pygame.Rect(0,0,width,height))
    self.rect = self.image.get_rect