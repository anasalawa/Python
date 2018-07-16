# Draw a bullseye
# 25 pixel width
# 5 red rings
# 5 grey rings
# 10 total
from SimpleGraphics import *

setColor("red")
ellipse(300,200,250,250)

i = 1
j = 0
w = 5
h = 5
for i in range(1,11):
	if j % 2 == 1:
		setColor("grey")
		ellipse(300,200,w,h)
		w = w + 5
		h = h + 5
	elif j % 2 == 0:
		setColor("grey")
		ellipse(300,200,w,h)
		w = w + 5
		h = h + 5













