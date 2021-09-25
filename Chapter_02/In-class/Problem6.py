# Calculate the slope of a line

x1 = float(input("What is the x coordinate of the first point? "))
x2 = float(input("What is the x coordinate of the second point? "))
y1 = float(input("What is the y coordinate of the first point? "))
y2 = float(input("What is the y coordinate of the second point? "))

slope = (y2 - y1) / (x2 - x1)

print("The slope of the line is", str(slope) + ".")
