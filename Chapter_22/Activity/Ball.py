from Point import *

from cs1graphics import *
from random import randint

class Ball:
  """
  A class used to represent a ball moving around in a canvas. The balls are run through a simulation.
  """

  _width = 500
  _height = 500
  _ballRadius = 10
  _maxSpeed = 100

  def __init__(self):    
    """ 
    Initializes the values of the Ball class.
    """
    x = randint(Ball._ballRadius, Ball._width - Ball._ballRadius)
    y = randint(Ball._ballRadius, Ball._height - Ball._ballRadius)
    self._position = Point(x, y)

    xVel = randint(-Ball._maxSpeed, Ball._maxSpeed)
    yVel = randint(-Ball._maxSpeed, Ball._maxSpeed)
    self._velocity = Point(xVel, yVel)

    self._graphics = Circle(Ball._ballRadius)
    randColor = (randint(0,255), randint(0,255), randint(0,255))
    self._graphics.setFillColor(randColor)
    self._graphics.moveTo(self._position.getX(), self._position.getY())
    
  def getGraphicalRep(self):
    """
    Returns the image on the canvas.
    """
    return self._graphics
    
  def getPosition(self):
    """
    Gets the position of the ball.
    """
    return self._position
    
  def getVelocity(self):
    """
    Gets the velocity of the ball.
    """
    return self._velocity
    
  def setPosition(self, p):
    """
    Sets the position of the ball.

    The value should be numeric.
    """
    self._position = p
    
  def setVelocity(self, v):
    """
    Sets the ball's velocity.

    The value should be numeric.
    """
    self._velocity = v

  def update(self, timeStep):
    """
    Starts the simulation of the balls.
    """
    self._position = self._position + self._velocity * timeStep

    if self._position.getX() < Ball._ballRadius:
      self._position.setX(Ball._ballRadius)
      self._velocity.setX(-self._velocity.getX())
    elif self._position.getX() > Ball._width - Ball._ballRadius:
      self._position.setX(Ball._width - Ball._ballRadius)
      self._velocity.setX(-self._velocity.getX())

    if self._position.getY() < Ball._ballRadius:
      self._position.setY(Ball._ballRadius)
      self._velocity.setY(-self._velocity.getY())
    elif self._position.getY() > Ball._height - Ball._ballRadius:
      self._position.setY(Ball._height - Ball._ballRadius)
      self._velocity.setY(-self._velocity.getY())
      
    self._graphics.moveTo(self._position.getX(), self._position.getY())

