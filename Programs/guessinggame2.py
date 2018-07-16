# Create an empty list
data = []

# Read the input from the user
value = input("Enter a value (blank line to quit): ")

# Create a loop with the range as the list
while value != "":
	# append the value into the list
	data.append(float(value))
	# Read the input again
	value = input("Enter a value (blank line to quit): ")

# Sort
data.sort()

if len(data) == 0:
	print("The list has no median value")

elif len(data) % 2 == 1:
	# The median is the middle value
	print("The median is", data[len(data) // 2])

else:
	# The median is the average the two values
	print("The median is", 
		(data[len(data) // 2] + data[(len(data) // 2) - 1]))


