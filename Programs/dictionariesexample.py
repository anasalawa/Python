# Compute the mode of a collection of values entered by the user

# Read all of the values from user and store them in a list
data = []
item = input("Enter a value (blank line to quit): ")
while item != "":
	data.append(item)
	item = input("Enter a value (blank line to quit): ")

# Compute the mode of the list
 
# Creates a new, empty dictionary
counts = {} 
# 	- Determine how many tiems each value occurs in the list
for item in data:
	# if this is an item that we have never encountered previously
	if item not in counts.keys():
		counts[item] = 1	
		# Insert item into the dictionary with count of 1
	# otherwise it is an item that we have seen before
	else:
		counts[item] = counts[item] + 1	
		# increase the count associated with that item
# 	- Report the values that occurred the largest number of times
if len(counts) > 0:
	print("The mode of modes of the list is/are: ")
	largest = max(counts.values())
	for k in counts.keys():
		if counts[k] == largest:
			print(k)
else:
	print("There weren't any values in the list.")