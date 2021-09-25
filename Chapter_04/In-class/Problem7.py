# PACMAN!

from cs1graphics import *

paper = Canvas(400, 400, 'black', 'PINK PACMAN')
head = Circle(150)
feet = Polygon(Point(50, 200), Point(50, 400), Point(100, 350), Point(150, 400), Point(200, 350), Point(250, 400), Point(300, 350), Point(350, 400), Point(350, 200))
eyeball1 = Circle(25)
eyeball2 = Circle(25)
pupil1 = Circle(10)
pupil2 = Circle(10)

head.moveTo(200, 200)
eyeball1.moveTo(150, 150)
eyeball2.moveTo(250, 150)
pupil1.moveTo(162.5, 150)
pupil2.moveTo(262.5, 150)

paper.add(head)
paper.add(feet)
paper.add(eyeball1)
paper.add(eyeball2)
paper.add(pupil1)
paper.add(pupil2)

head.setFillColor('pink')
feet.setFillColor('pink')
eyeball1.setFillColor('white')
eyeball2.setFillColor('white')
pupil1.setFillColor('black')
pupil2.setFillColor('black')
feet.setBorderWidth(0)
eyeball1.setBorderWidth(0)
eyeball2.setBorderWidth(0)
