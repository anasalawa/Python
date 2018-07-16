# Compute the sum of a collection of numbers stating
# number on each line

# Read the name of the file from the user
import sys

# Verify that a filename was provided as part of the comamnd used to
# start the program

if len(sys.argv) != 2:
	print("give me a filename hoe")
	print("")
	print("python3 fileexample.py <filename>")
	quit()


# Open the file for reading
inf = open(sys.argv[1], "r")

# Read the contents of the file, adding each variable
total = 0
line = inf.readline()

# While there is still data in the file
while line != "":
	# Remove the newline character
	line = line.rstrip()
	# Display the number before adding it to the line
	print("About to add", line, "to the total...")
	# Add the current value to the total
	total = total + float(line)

	line = inf.readline()

# Display the result
print("The sum of the numbers in", sys.argv[1],"blah blah")

# Close the file
inf.close()
