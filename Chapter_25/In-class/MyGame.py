from BallGame import *
from Wall import *
from Obstacle import *
##from RedObstacle import *
##from PurpleObstacle import *
from GreenObstacle import *

game = BallGame(width=800, height=650, maxSpeed=250,
			moveDir='mouse dir')
##                        moveDir='to mouse')

for i in range(10):
    w = Wall (400, 325+i*50, 400, 5)
    game.addWall (w)

for i in range(10):
  b = Obstacle (maxSpeed=150)
  game.addObstacle (b)

b2 = GreenObstacle (maxSpeed=50, ballRadius=20)
game.addObstacle (b2)

game.run()
