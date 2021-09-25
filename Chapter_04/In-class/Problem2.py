# House

from cs1graphics import *

paper = Canvas(800, 500)
house = Rectangle(400, 200)
door = Rectangle(75, 150)
roof = Polygon(Point(400, 100), Point(150, 200), Point(650, 200))
doorHandle = Circle(1)

paper.add(house)
paper.add(door)
paper.add(roof)
paper.add(doorHandle)

house.moveTo(400, 300)
door.moveTo(400, 325)
doorHandle.moveTo(420, 340)

