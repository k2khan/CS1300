from Point import *
from Obstacle import *

import cs1graphics
from random import randint

class CyanObstacle(Obstacle):
  def __init__(self, maxSpeed=50, ballRadius=30, color='cyan'):    
    super().__init__(maxSpeed, ballRadius, color)
    
  def interact(self, other, game):
    if self.checkCollision(other):
      other.speedMult(3, 3)

      # Also handle collisions
      self.checkCollision (other)

