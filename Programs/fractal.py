# Draw the fractal T square using recursion
from SimpleGraphics import *
from random import randrange

def tsquare(x, y, w, h):
	setColor(x / getWidth() * 255, y / getHeight() * 255, randrange(0, 256))
	rect(x + w/4, y + h/4, w/2, h/2)
	if w > 4 and h > 4:
		tsquare(x, y, w/2, h/2)
		tsquare(x + w/2, y, w/2, h/2)
		tsquare(x + w/2, y + h/2, w/2, h/2)


def main():
	setColor("black")
	background("white")
	tsquare(getWidth() / 2 - 256, getHeight() / 2 - 256, 512, 512)

main()