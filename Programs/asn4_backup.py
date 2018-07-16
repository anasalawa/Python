# Anas Alawa | 30016568 L02 T11
# Importing all the required files
import sys
import formatList

# def main():
# Taking the input filename from the user
if len(sys.argv) == 1:
	fileName = input("Enter the name of a file: ")

# If the number of elements given by the user aren't two
# Prompt them to write it the write way and quit the program
elif len(sys.argv) == 2:
	fileName = sys.argv[1]

else:
	print("python3 fileexample.py <filename>")
	quit()

file = open(fileName, "r")

# PART 1: Creating the dictionary
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

# def relation():
predList = foodweb.keys()
for pred in sorted(predList):
	print(" ", pred, "eats", formatList.formatList(foodweb[pred]))

# PART 2: APEX PREDATOR
preyList = []
for pred in foodweb.keys():
	for prey in foodweb[pred]:
		if prey not in preyList:
			preyList.append(prey)


apexPred = []
for pred in foodweb.keys():
	if pred not in preyList:
		apexPred.append(pred)
print("\nApex Predator(s):", formatList.formatList(apexPred))

# PART 3: IDENTIFYING THE PRODUCERS
producer = []
for prey in preyList:
	if prey not in foodweb.keys():
		producer.append(prey)
print("Producer(s):", formatList.formatList(producer))

# PART 4: IDENTIFY THE MOST FLEXIBLE EATER
flexible = []
counts = {}
for pred in foodweb.keys():
		counts[pred] = [len(foodweb[pred])]
freq = max(counts.values())
for pred in counts.keys():
	if counts[pred] == freq:
		flexible.append(pred) 

print("Most Flexible Eater(s):", formatList.formatList(flexible))

# PART 5: THE TASTIEST ORGANISM
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

print("Tastiest:", formatList.formatList(mode))


# PART 6: THE HEIGHT OF EACH ORGANISM
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

for animal in sorted(height.keys()):
	print(" ", animal + ":", height[animal])

# Closing the file
file.close()