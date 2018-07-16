# Anas Alawa | 30016568 L02 T11
# This program will create and analyze foodwebs and the relationship
	# between predators and prey

# Importing all the required files/libraries
import sys
import formatList

# Defining the main function that will tie together all the other functions
# This function will be called on at the end
# This function will call upon all the other functions that are made
def main():
	# If the number of elements given by the user equals to one
	# Taking the input filename from the user
	if len(sys.argv) == 1:
		fileName = input("Enter the name of a file: ")

	# If the number of elements given by the user equals to two
	# Set the fileName as the file inputted by the user
	elif len(sys.argv) == 2:
		fileName = sys.argv[1]

	# Otherwise, demonstrate proper format and quit the program
	else:
		print("Please enter using this format: python3 fileexample.py <filename>")
		quit()

	# Opening the file and reading it
	# If the file doesn't exist, display an error message
	try:
		file = open(fileName, "r")
	except FileNotFoundError:
		print("The file entered does not exist.")
		quit()


# PART 1: CREATING THE DICTIONARY
	# Reads through the file and creates the foodweb dictionary
	# The foodweb dictionary contains predator and prey relationships
	# Assigns predators as keys and preys as values
	foodweb = {}
	print("Predators and Prey:")
	for line in file:
		line = line.rstrip()
		animals = line.split(" eats ")
		pred = animals[0]
		prey = animals[1]
		if pred in foodweb.keys():
			foodweb[pred].append(prey)
		else:
			foodweb[pred] = [prey]

	# Calling on ALL defined functions:
	predList = relation(foodweb)
	for pred in sorted(predList):
		print(" ", pred, "eats", formatList.formatList(foodweb[pred]))

	preyList = preys(foodweb)

	apexPred = apexPredator(foodweb)
	print("\nApex Predator(s):", formatList.formatList(apexPred))

	producer = prod(foodweb)
	print("Producer(s):", formatList.formatList(producer))

	flexible = flexEater(foodweb)
	print("Most Flexible Eater(s):", formatList.formatList(flexible))

	mode = taste(foodweb)
	print("Tastiest:", formatList.formatList(mode))

	height = org_height(foodweb)
	for animal in sorted(height.keys()):
		print(" ", animal + ":", height[animal])

	# Closing the file
	file.close()


# Defining a function that creates and returns a predator list
# This function will take the foodweb dictionary as a parameter 
def relation(foodweb):
	predList = foodweb.keys()
	return predList


# Defining a function that creates and returns a prey list
# This function will be called upon in other functions
# This function will take the foodweb dictionary as a parameter 
def preys(foodweb):
	preyList = []
	for pred in foodweb.keys():
		for prey in foodweb[pred]:
			if prey not in preyList:
				preyList.append(prey)

	return preyList


# PART 2: APEX PREDATOR
	# This function will create and return an apex predator list
	# This function will call upon the preys function
	# This function will take the foodweb dictionary as a parameter 
def apexPredator(foodweb):	
	preyList = preys(foodweb)
	apexPred = []
	for pred in foodweb.keys():
		if pred not in preyList:
			apexPred.append(pred)

	return apexPred


# PART 3: IDENTIFYING THE PRODUCERS
	# This function will call upon the preys function
	# This function will create and return a list of producers
	# This function will take the foodweb dictionary as a parameter 
def prod(foodweb):
	preyList = preys(foodweb)
	producer = []
	for prey in preyList:
		if prey not in foodweb.keys():
			producer.append(prey)

	return producer


# PART 4: IDENTIFY THE MOST FLEXIBLE EATER
	# This function will create and return a list of flexible eaters
	# A counts dictionary is created to count the frequency 
	# This function will take the foodweb dictionary as a parameter 
def flexEater(foodweb):
	flexible = []
	counts = {}
	for pred in foodweb.keys():
			counts[pred] = [len(foodweb[pred])]
	freq = max(counts.values())
	for pred in counts.keys():
		if counts[pred] == freq:
			flexible.append(pred) 

	return flexible


# PART 5: THE TASTIEST ORGANISM
	# This function will create and return a list called the mode
	# A tastiest list is created to locate the tastiest animals	
	# A counts dictionary is created to count the frequency
	# This function will take the foodweb dictionary as a parameter 
def taste(foodweb):
	mode = []
	tastiest = []
	counts = {}
	for pred in foodweb.keys():
		for prey in foodweb[pred]:
			tastiest.append(prey)

	for prey in tastiest:
		if prey not in counts.keys():
			counts[prey] = 1
		else:
			counts[prey] = counts[prey] + 1

	freq = max(counts.values())
	for prey in counts.keys():
		if counts[prey] == freq:
			mode.append(prey) 

	return mode


# PART 6: THE HEIGHT OF EACH ORGANISM
	# This function will call upon the preys function	
	# This function will create and return a dictionary that measures the height
	# A boolean called change is setup to mark if any changes have occurred
	# This function will take the foodweb dictionary as a parameter 
def org_height(foodweb):
	preyList = preys(foodweb)
	height = {}
	print("\n Heights:")
	for pred in foodweb.keys():
		height[pred] = 0

	for prey in preyList:
		height[prey] = 0

	change = True
	while change == True:
		change = False
		for pred in foodweb.keys():
			for prey in foodweb[pred]:

				if height[pred] <= height[prey]:
					height[pred] = height[prey] + 1
					change = True

	return height

# Calling the main function
main()