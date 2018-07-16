from SimpleGraphics import *

setColor("red")
ellipse(100,100,25,25)

circle = 1
x = 150
# green horizontal
for circle in range(1,8):
	setColor("green")
	ellipse(x,100,25,25)
	x = x + 50
	circle = circle + 1

circle = 1
y = 150
# blue vertical
for circle in range(1,6):
	setColor("blue")
	ellipse(100,y,25,25)
	y = y + 50
	circle = circle + 1