# Compute the average of a collection of numbers entered by the user.
# The user will enter Enter to indicate that no more values will be entered
# and the average should be displayed.

value = input("Enter a number (Enter to quit): ")

total = 0
count  = 0


# Read values until the user enters 0
while value != "":
	total = total + float(value)
	count = count + 1

	value = input("Enter a number (Enter to quit): ")

if count == 0:
	print("No values were entered.")
else:
	print ("The average of those numbers is ", total / count)