# Snowman

from cs1graphics import *

# Create objects
paper = Canvas(500, 1000, 'skyBlue', 'Snowman')
head = Circle(100)
stomach = Circle(150)
thighs = Circle(200)
eye1 = Circle(10)
eye2 = Circle(10)

paper.add(head)
paper.add(stomach)
paper.add(thighs)
paper.add(eye1)
paper.add(eye2)

head.moveTo(250, 200)
stomach.moveTo(250, 400)
thighs.moveTo(250, 700)
eye1.moveTo(225, 185)
eye2.moveTo(275, 185)

head.setFillColor('white')
stomach.setFillColor('white')
thighs.setFillColor('white')
eye1.setFillColor('black')
eye2.setFillColor('black')

thighs.setDepth(100)
stomach.setDepth(90)
head.setDepth(60)
