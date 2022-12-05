import pygame

#this creates the coins that the player collects
class Coin(pygame.sprite.Sprite):
  def __init__(self,x,y):
    super().__init__()
    self.sprites = []
    self.sprites.append(pygame.image.load('assets/Sprites/Items/coin.png'))
    self.sprites.append(pygame.image.load('assets/Sprites/Items/coin2.png'))
    self.sprites.append(pygame.image.load('assets/Sprites/Items/coin3.png'))
    self.current_sprite = 0
    self.x = 0
    self.y = 0
    self.image = pygame.Surface((4,16))
    self.rect = self.image.get_rect(topleft = [x,y])
    self.image = self.sprites[self.current_sprite]
    self.is_active = True
    self.is_colliding = False

  def delete(self):
    self.image = pygame.Surface((0,0))

  def update(self, surface):
    if self.is_active == True:
      self.current_sprite += 0.17
      if self.current_sprite >= len(self.sprites):
        self.current_sprite = 0
      self.image = self.sprites[int(self.current_sprite)]
    if self.is_colliding == True:
      surface.blit(self.image, self.rect)


  #def collect_coin(self, Player1):
    #for c in coin:
      #if c.colliderect(Player_rect):
        #coin.remove(c)
        #score += 1
      