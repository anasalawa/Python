# Compute the number of lines, words, and characters in a file.
import sys

# Open the file for reading and 2nd one for writing
if len(sys.argv) != 2:
	print("The program must be started with two command line parameters!")
	print("   1) The name of the file to read")
	print("   2) The name of the file where the results will be saved")
	quit()

inf = open(sys.argv[1], "r") # Opening the file for reading
outf = open(sys.argv[2], "w") # Opening the file for writing

lines = 0
words = 0
chars = 0
# Process each line in the file
line = inf.readline()
while line != "":
	# Count the line
	lines = lines + 1
	# Count the # of words
	words = words + len(line.split()) # this will split at every space
									  # and return it as a list
	# Count the # of characters
	chars = chars + len(line) # this checks the length of the string
	# Read the next line from the file
	line = inf.readline()

# Report the results
outf.write("In the file there were:\n ")
outf.write("  " + str(lines) + " lines\n")
outf.write("  " + str(words) + " words\n")
outf.write("  " + str(chars) + " chars\n")

inf.close()
outf.close()