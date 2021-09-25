# Mickey Mouse

from cs1graphics import *

# Create variable
w = 300
h = w

# Create objects
paper = Canvas(w, h)
ear1 = Circle(w * 3/20)
ear2 = Circle(w * 3/20)
face = Circle(w * 3/10)

# Add and set color
paper.add(ear1)
paper.add(ear2)
paper.add(face)
ear1.moveTo(1/5 * w, 1/5 * h)
ear1.setFillColor('black')
ear2.moveTo(4/5 * w, 1/5 * h)
ear2.setFillColor('black')
face.moveTo(1/2 * w, 1/2 * h)
face.setFillColor('black')

