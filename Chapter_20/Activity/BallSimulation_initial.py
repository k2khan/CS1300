from Point import *

from cs1graphics import *
from random import randint
from time import sleep, time

class Ball:
  def __init__(self, width=500, height=500):
    self._width = width
    self._height = height    
    self._ballRadius = 10
    maxSpeed = 100
    
    x = randint(self._ballRadius, width - self._ballRadius)
    y = randint(self._ballRadius, height - self._ballRadius)
    self._position = Point(x, y)

    xVel = randint(-maxSpeed, maxSpeed)
    yVel = randint(-maxSpeed, maxSpeed)
    self._velocity = Point(xVel, yVel)

    self._graphics = Circle(self._ballRadius)
    self._graphics.setFillColor('red')
    self._graphics.moveTo(self._position.getX(), self._position.getY())
    
  def getGraphicalRep(self):
    return self._graphics
    
  def update(self, timeStep):
    self._position = self._position + self._velocity * timeStep

    if self._position.getX() < self._ballRadius:
      self._position.setX(self._ballRadius)
      self._velocity.setX(-self._velocity.getX())
    elif self._position.getX() > self._width - self._ballRadius:
      self._position.setX(self._width - self._ballRadius)
      self._velocity.setX(-self._velocity.getX())

    if self._position.getY() < self._ballRadius:
      self._position.setY(self._ballRadius)
      self._velocity.setY(-self._velocity.getY())
    elif self._position.getY() > self._height - self._ballRadius:
      self._position.setY(self._height - self._ballRadius)
      self._velocity.setY(-self._velocity.getY())
      
    self._graphics.moveTo(self._position.getX(), self._position.getY())

# Initialize the balls
paper = Canvas(500, 500)
paper.setAutoRefresh(False)
balls = []
for i in range(25):
  b = Ball()
  paper.add(b.getGraphicalRep())
  balls.append(b)
paper.refresh()

# Move the balls
lastUpdateTime = time()
while True:
  currentTime = time()
  timeStep = currentTime - lastUpdateTime
  for b in balls:
    b.update(timeStep)
  paper.refresh()
  lastUpdateTime = currentTime
