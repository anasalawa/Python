# Count the number of times that what occurs in data
def countItems(data, what):
	count = 0
	for item in data:
		if item == what:
			count = count + 1
	return count

# Count the number of times that what occurs in data
def countItems2(data, what):
	count = 0
	while len(data) > 0:
		if data.pop() == what:
			count = count + 1
	return count

values = [1,2,1,3,1,2,3,4]
print("1 occurs in values", countItems(values, 1), "times using countItems.")
print("1 occurs in values", countItems2(values, 1), "times using countItems.")

# if you inverse the order of the print statements, the program will
# no longer work because you are using the method data.pop()