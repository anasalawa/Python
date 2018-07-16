# The purpose of this assignment is to create a face using
# the SimpleGraphics library.
# Anas Alawa
# 30016568

from SimpleGraphics import *

# Background
background("cornflower blue")

# L Leg 
setOutline("black")
setFill("dark red")
rect(220, 100, 120, 350)

# R Leg
setOutline("black")
setFill("dark red")
rect(462.5, 100, 120, 350)

# R Arm :
# Fist
setOutline("black")
setFill("dark red")
ellipse(655, 130, 110, 75)

# Arm
setColor("dark red")
rect(670, 314, 80, -160)
rect(570, 225, 150, 90)

# Bicep
ellipse(580, 200, 90, 70)

# Fingers
setColor("black")
line(690, 134, 690, 160)
line(710, 132, 710, 162)
line(730, 134, 730, 160)

# L Arm : 
# Fist
setOutline("black")
setFill("dark red")
ellipse(35, 130, 110, 75)

# Arms
setColor("dark red")
rect(130, 314, -80, -160)
rect(220, 225, -150, 90)

# Bicep
ellipse(133, 200, 90, 70)

# Fingers
setColor("black")
line(70, 134, 70, 160)
line(90, 132, 90, 162)
line(110, 134, 110, 160)

# Body
setColor("dark red")
rect(230, 100, 340, 300)

# L then R Eyes
setColor("black")
ellipse(270, 150, 80, 80)

setColor("black")
ellipse(450, 150, 80, 80)

setColor("lavender")
ellipse(275, 160, 30, 45)

setColor("lavender")
ellipse(460, 160, 30, 45)

# Mouth
setColor("black")
blob(320, 300, 420, 400, 520, 250, 270, 250)

# Tongue
setOutline("black")
setFill("hot pink")
ellipse(375, 360, 75, -35)
line(410, 280, 410, 370)

# Name
setColor("black")
setFont("Times", "15", "italic")
text(750, 590, "Anas Alawa")



