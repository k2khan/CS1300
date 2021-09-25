from cs1graphics import *


w = 200
h = 300
paper = Canvas(w, h)

circle1 = Circle(w * 1/4)
circle1.setFillColor('pink')
circle1.setBorderWidth(0)
circle1.moveTo(w * 1/2, h * 1/4)
paper.add(circle1)

circle2 = Circle(w * 1/4)
circle2.setFillColor('pink')
circle2.setBorderWidth(0)
circle2.moveTo(w * 1/2, h * 1/2)
paper.add(circle2)

cone = Polygon(Point(w * 1/2, h), Point(w * 1/4, h * 1/2), Point(w * 3/4, h * 1/2))
cone.setFillColor('sandybrown')
cone.setBorderWidth(0)
paper.add(cone)
