from Point import *

from Obstacle import *

import cs1graphics
from random import randint

class RedObstacle(Ball):
  def __init__(self, maxSpeed=100, ballRadius=10, color='red'):    
    super().__init__(maxSpeed, ballRadius, color)

  def checkCollision (self, other):
    if isinstance (other, Ball):
      if self.distance(other) < (self.getRadius() + other.getRadius()):
        self.collision (other)
        return True
      else:
        return False
    elif isinstance (other, Wall):
      return True
    else:
      return False
    
  def interact(self, other, game):
    if self.checkCollision (other):
      game.adjustPoints (-1)

