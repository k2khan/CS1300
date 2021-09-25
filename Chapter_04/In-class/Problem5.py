# Peace sign

from cs1graphics import *

paper = Canvas(500, 500, 'pink', 'peace sign')
outerCircle = Circle(200)
middleLine = Path(Point(250, 50), Point(250, 450))
leftLine = Path(Point(250, 250), Point(110, 390))
rightLine = Path(Point(250, 250), Point(390, 390))

paper.add(outerCircle)
paper.add(middleLine)
paper.add(leftLine)
paper.add(rightLine)

outerCircle.moveTo(250, 250)
outerCircle.setBorderWidth(5)
middleLine.setBorderWidth(5)
leftLine.setBorderWidth(5)
rightLine.setBorderWidth(5)

outerCircle.setFillColor('white')
