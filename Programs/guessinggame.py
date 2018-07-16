# create an empty list
data = []

# read the first input value
value = input("Enter a value (blank to quit): ")

# while the value entered the user is not blank
	# add the value to a list (make sure you convert to float)
	# "" means the user would enter a blank line
	# read the next input value
while value != "":
	data.append(float(value))
	value = input("Enter a value (blank to quit): ")


# Sort the list

data.sort()

# If the length of the list == 0
	# Report that "There is not a median value"
if len(data) == 0:
	print("There is no median value for this list.")

# Elif the length of the list is odd 
	# Report the middle value as the median
	# Divide by 2 using integer division
elif len(data) % 2 == 1:
	print("The middle value is", data[len(data) // 2])

# Else:
	# Report the average of the two middle values as the median
else:
	print("The median value is",
		(data[len(data) // 2] + data[(len(data) // 2 - 1)]))
