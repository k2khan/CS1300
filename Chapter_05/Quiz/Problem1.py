from cs1graphics import *
from time import sleep

paper = Canvas(500, 500)

red = Square(100)
red.setFillColor('red')
red.moveTo(50, 50)
red.setBorderWidth(0)
paper.add(red)

L = Layer()
paper.add(L)
rectangle = Rectangle(100, 400)
rectangle.setFillColor('blue')
L.add(rectangle)
rectangle.moveTo(50, 300)
L.adjustReference(100, 100)

for i in range(1, 100):
    L.rotate(-1)
    sleep(0.033)

