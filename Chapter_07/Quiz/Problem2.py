from cs1graphics import *
from math import *

paper = Canvas(1000, 400, 'black')
numWidth = 10
numHeight = 4

# First diamond
square = Square(50*sqrt(2), Point(50, 50))        
square.rotate(45)
paper.add(square)
square.setFillColor('gray')

# Loop through for the rest of the diamonds
for i in range(numWidth):
    square = Square(50*sqrt(2), Point(50, 50))        
    square.rotate(45)
    square.moveTo(50 + 100 * i , 50)
    paper.add(square)
    square.setFillColor('gray')
    for x in range(numHeight):
        square = Square(50*sqrt(2), Point(50, 50))        
        square.rotate(45)
        square.moveTo(50 + 100 * i , 50 + 100 * x)
        paper.add(square)
        square.setFillColor('gray')
