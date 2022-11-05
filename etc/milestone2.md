# Final Project Milestone #2

[Final Project Description](https://docs.google.com/document/d/1j3zgypVjPjzXl4pL1_Wpjvp3GLCW9zcFydkwUjNfNUA/edit?usp=sharing)

Complete this document in **your** portfolio (CH 6). 

Let's decide on our Final project. Select the idea from Milestone 1 that seems the most interesting to you.

Each class is a model of some real world object. We often refer to data classes as the ***models*** in a GUI program. Your models represent your application data.

Given what you have learned about classes on Chapter 6, describe the ***interface only*** of 3 classes you think you might need for your project.

*For example*, if you want to create a space invaders type game, you would need a class to represent the ship, which could have an interface such as: 

* class ship
    * moveLeft()
    * moveRight()
    * shoot()

***

Come up with interfaces fot 3 possible classes you think you may need. Again, brainstorm a little. Nothing is *wrong*.

## Class Interface 1

Class Player:
  def __init__(self, P1posx, P1posy, P1width, P1height):
    self.x = P1posx
    self.y = P1posy
    self.width = P1width
    self.height = P1height
    self.color = color

  def move(P1posx,P1posy):
    if key == a:
      P1posx += 1
    if key == s:
      P1posx -= 1 

  def jump(P1posx,P1posy):
    if is_on_floor():
      if key == k:
        P1posy -= 5
       
    

## Class Interface 2

Class Coin
  def __init__(self, posx=0, posy=0, width, height, color):
    self.x = posx
    self.y = posy
    self.width = width
    self.height = height
    self.color = color

  def collide()
    if P1posx >= posx or P1posx <= posx or P1posy >= posy or P1psy <=posy:
      points += 1
      
  

## Class Interface 3

Class Enemy
  def __init__(self, posx, posy, width, height, color):
    self.x = posx
    self.y = posy
    self.width = width
    self.height = height
    self.color = color

  def def collide()
    if P1posx >= posx or P1posx <= posx or P1posy >= posy or P1psy <=posy:
      posx -= 5
    if P1posx <= posx:
      posx += 5
    if P1posy <= posy:
      squish()
    if P1posy >= posy:
      posy -= 5
        

