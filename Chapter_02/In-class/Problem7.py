# Find the distance between two points

x1 = float(input("What is the x coordinate of the first point? "))
y1 = float(input("What is the y coordinate of the first point? "))
x2 = float(input("What is the x coordinate of the second point? "))
y2 = float(input("What is the y coordinate of the second point? "))

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print("The distance between the two points is", str(distance) + ".")
