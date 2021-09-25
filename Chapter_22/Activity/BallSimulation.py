from Ball import *

from time import sleep, time

class BallSimulation:
  def __init__(self, numberOfBalls=25, width=500, height=500, ballRadius=10, maxSpeed=100):
    # BallSimulation can re-define Ball's class variables, as desired
    Ball._width = width
    Ball._height = height
    Ball._ballRadius = ballRadius
    Ball._maxSpeed = maxSpeed

    self._paper = Canvas(width, height)
    self._paper.setAutoRefresh(False)
    self._balls = []
    for i in range(numberOfBalls):
      b = Ball()
      self._paper.add(b.getGraphicalRep())
      self._balls.append(b)
    self._paper.refresh()

  def run(self):
    lastUpdateTime = time()
    while True:
      currentTime = time()
      timeStep = currentTime - lastUpdateTime
      for b in self._balls:
        b.update(timeStep)
        
      # check balls for collisions
      for i in range(len(self._balls)):
        # only need to check balls at index i with those at index >i  (rest already checked)
        for b2 in self._balls[i+1:]:
          if self._balls[i].getPosition().distance(b2.getPosition()) < 2*Ball._ballRadius:
            self._collision(self._balls[i], b2)
        
      self._paper.refresh()
      lastUpdateTime = currentTime

  def _collision(self, ball1, ball2):
    p = ball1.getPosition() - ball2.getPosition()
    p.normalize()
    v = ball2.getVelocity() - ball1.getVelocity()
    
    if p * v > 0:
      alpha = p*v
      
      ball1.setVelocity( ball1.getVelocity() + alpha*p ) 
      ball2.setVelocity( ball2.getVelocity() - alpha*p ) 


if __name__ == '__main__':
    sim = BallSimulation(30, width=1500, height=750, maxSpeed=250)
    sim.run()
