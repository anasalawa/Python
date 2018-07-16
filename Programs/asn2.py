# Anas Alawa | 30016568 | L02 | T11
# Making an accurate climograph
from SimpleGraphics import *
background("white")

# Temp Axis (1 degree is 10 pixels) 
setFont("Times", "12")
text(50, 250, "Temperature")
text(50, 265, "(Celsius)")
line(100, 100, 100, 500)

# temperature small ticks
for temp_tick in range(400, 99, -100):
	line(95, temp_tick, 100, temp_tick)

for t_text in range(-20, 21, 10):
	text(85, ((t_text * -10) + 300), str(t_text))

# Precip Axis (1 mm is 2 pixels ~ 20 mm is 40 pixels) 
text(770, 250, "Precip.")
text(770, 265, "(mm)")
line(700, 100, 700, 500)

# preciptation small ticks
for precip_tick in range(100, 461, 40):
	line(700, precip_tick, 705, precip_tick)

# looping the text for precipitation
for p_text in range(0, 201, 20):
	text(720, ((p_text * -2) + 500), str(p_text))

# Months axis (text) 50 pixels for each month
line(95, 500, 705, 500)
text(125, 520, "Jan")
text(175, 520, "Feb")
text(225, 520, "Mar")
text(275, 520, "Apr")
text(325, 520, "May")
text(375, 520, "Jun")
text(425, 520, "Jul")
text(475, 520, "Aug")
text(525, 520, "Sep")
text(575, 520, "Oct")
text(625, 520, "Nov")
text(675, 520, "Dec")

# Precipitation calculations
month = 1
while month <= 12:
	# Prompt input from user
	precip = float(input("Enter a precipitation value for month " + str(month) + " : "))
	setFill("steel blue")
	# Bars for precipitation
	rect(((month * 50) + 55), 500, 40, (precip * -2))
	month = month + 1
	
# Temperature calculations
month = 1
while month <= 12:
	temp = float(input("Enter a temperature value for month " + str(month) + " : "))
	setColor("red3")
	ellipse((month * 50) + 75, (temp * -10) + 300, 7, 7)
	# Connect the dots (preceding x and y connecting to the month that follows)
	if month != 1:
		line(preced_x, preced_y, (month * 50) + 78, (temp * -10) + 302.5)
	preced_x = (month * 50) + 78
	preced_y = (temp * -10) + 302.5
	month = month + 1