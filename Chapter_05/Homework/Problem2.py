from cs1graphics import *

paper = Canvas(500, 300)

stuff = Layer()

box = Rectangle(200, 100, Point(250, 200))
box.setBorderWidth(2)
stuff.add(box)

circle = Circle(50, Point(350, 150))
circle.setFillColor('red')
circle.setBorderWidth(2)
stuff.add(circle)

paper.add(stuff)
stuff.adjustReference(350, 150)
stuff.rotate(30)
