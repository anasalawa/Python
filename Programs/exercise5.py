# Anas Alawa | 30016568 | L02 T11
# Write a program that collects values from a user
# Display the values in opposite order

# Creating an empty list
data = []

# Reading the input
value = input("Enter a value (blank line to quit): ")

# Inserting the values in opposite order
# Reading the input again
while value != "":
	data.insert(0,value)
	value = input("Enter a value (blank line to quit): ")

# Printing values in rows
for item in data:
		print(item)
