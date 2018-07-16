#Converting from a letter grade into the equivalent number of grade points
# A = 4.0
# B = 3.0
# C = 2.0
# D = 1.0
# F = 0.0

letter = input("What is your letter grade? ")

# if statement for the # of gradepoints for the entered letter

if letter == "A" or letter == "a":
	gp = 4.0

elif letter == "B" or letter == "b":
	gp = 3.0

elif letter == "C" or letter == "c":
	gp = 2.0

elif letter == "D" or letter == "d":
	gp = 1.0

elif letter == "F" or letter == "f":
	gp = 0.0

else:
	gp = -1.0

# Print the number of grade points.
if gp >= 0.0:
	print ("The letter grade", letter, "is equal to", gp, "grade points.")

else:
	print("Please enter a valid letter grade ranging from A to F")