from cs1graphics import *

numLevels = 8
unitSize = 12

screenSize = unitSize * (numLevels + 1)
paper = Canvas(screenSize, screenSize)

for level in range(numLevels):
    width = (level + 1) * unitSize
    block = Rectangle(width, unitSize)
    centerY = (level + 1) * unitSize
    centerX = screenSize - (1/2 * width) - 6
    block.move(centerX, centerY)
    block.setFillColor('gray')
    paper.add(block)
