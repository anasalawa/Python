# Generating a smooth color gradient from black to (255, 192, 64)
from SimpleGraphics import *

# for each line on the screen
for y in range(0, getHeight()):
	# set the color for the current row
	r = y / (getHeight() - 1) * 255
	g = y / (getHeight() - 1) * 192
	b = y / (getHeight() - 1) * 64
	setColor(r, g, b)

	# Draw the line for the current row
	line(0, y, getWidth() - 1, y)