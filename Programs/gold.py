# Report the state of some gold based on a temperature entered by
# the user.

#Read the temperature from the user
temp = float(input("Enter the temperature of some gold: "))

#Determine the state of the gold from the entered temperauture
if temp < 1064:
	state = "solid"
elif temp < 2807:
	state = "liquid"
else:
	state = "gas"

#Report the result to the user
print("At", temp, "degrees, gold is a", state)