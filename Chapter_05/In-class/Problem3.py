from cs1graphics import *
from time import sleep

paper = Canvas(400, 400)

propeller1 = Ellipse(35, 200)
propeller1.setFillColor('blue')
paper.add(propeller1)

propeller1.moveTo(200, 200)
propeller1.rotate(45)



while True:
    propeller1.rotate(1)
    sleep(0.033)
