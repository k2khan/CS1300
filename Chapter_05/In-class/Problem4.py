from cs1graphics import *

paper = Canvas(500, 500)

red = Square(100)
red.setFillColor('red')
red.moveTo(50, 450)
paper.add(red)

L = Layer()
paper.add(L)
rectangle = Rectangle(400, 100)
rectangle.setFillColor('blue')
L.add(rectangle)
L.moveTo(300, 450)
L.adjustReference(-200, -50)
L.rotate(-30)
