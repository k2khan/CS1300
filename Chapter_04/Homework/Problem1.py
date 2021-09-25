# Create a tree
from cs1graphics import *

# Create objects
tree = Canvas()
tree.setWidth(400)
tree.setHeight(500)
bush = Circle()
trunk = Rectangle(50, 175)
tree.add(bush)
tree.add(trunk)

# Set bush
bush.setRadius(100)
bush.moveTo(200, 200)
bush.setFillColor('green')

# Set trunk
trunk.moveTo(200, 362.5)
trunk.setFillColor('brown')

# Bring bush to front
bush.setDepth(25)
