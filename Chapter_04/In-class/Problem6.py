# Swiss flag

from cs1graphics import *

paper = Canvas(500, 500, 'red', 'swiss flag')
cross = Polygon(Point(200, 100), Point(300, 100), Point(300, 200), Point(400,200), Point(400, 300), Point(300, 300), Point(300, 400), Point(200, 400), Point(200, 300), Point(100, 300), Point(100, 200), Point(200, 200))

paper.add(cross)
cross.setFillColor('white')
cross.setBorderWidth(0)
