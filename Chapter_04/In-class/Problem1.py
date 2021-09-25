# Mickey Mouse

from cs1graphics import *

# Create objects
paper = Canvas(500, 500)
ear1 = Circle(75)
ear2 = Circle(75)
face = Circle(150)

# Add and set color
paper.add(ear1)
paper.add(ear2)
paper.add(face)
ear1.moveTo(100, 100)
ear1.setFillColor('black')
ear2.moveTo(400, 100)
ear2.setFillColor('black')
face.moveTo(250, 250)
face.setFillColor('black')
