# Using at most 3 ellipse commands
# Draw 13 circles with radius == 25
# Centers of adjacent circles 100 pixels apart
from SimpleGraphics import *

# While loop



setColor("red")
ellipse(100, 100, 25, 25)

# green horizontal
circle = 1

x = 150
while circle <= 7:
	setColor("green")
	ellipse(x, 100, 25, 25)
	x = x + 50
	circle = circle + 1
# blue vertical

circle = 1
y = 150
while circle <= 5:
	setColor("blue")
	ellipse(100, y, 25, 25)
	y = y + 50
	circle = circle + 1


