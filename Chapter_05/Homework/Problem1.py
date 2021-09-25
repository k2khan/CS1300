from cs1graphics import *


# Can change the width and height values.

w = 500
h = 300
paper = Canvas(w, h)

box = Rectangle(w * 2/5, h * 1/3, Point(w * 1/2, h * 2/3))
box.setBorderWidth(2)
paper.add(box)

circle = Circle(w * 1/10, Point(w * 7/10, h * 1/2))
circle.setFillColor('red')
circle.setBorderWidth(2)
paper.add(circle)

