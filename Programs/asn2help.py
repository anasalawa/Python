# Read integers from the user, and for each integer, report the difference
# between it and its immediate predecessor.

prev = int(input("Enter an integer (0 to quit): "))

while prev != 0:

	value = int(input("Enter an integer (0 to quit): "))
	print("The difference between", prev, "and", value, "is", value - prev)
	# this is the key element. use this when graphing temperature
	prev = value

