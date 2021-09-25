from Point import *
from Obstacle import *

import cs1graphics
from random import randint

class RemoveableObstacle(Obstacle):
  def __init__(self, maxSpeed=50, ballRadius=30, color='black'):    
    super().__init__(maxSpeed, ballRadius, color)
    
  def interact(self, other, game):
    if self.checkCollision(other):
      game.adjustPoints(3)
      game.deleteObstacle(self)

