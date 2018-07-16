# Play a number guessing agme with the user. The user should try and figure out what number the computer selected
# using as few guesses as possible.
import random

upper_limit = 100
lower_limit = 1

# Pick a random target number that the user is trying to guess
target = random.randrange(lower_limit, upper_limit + 1)

# Read a guess from the user
guess = int(input("Enter a guess between " + str(lower_limit) +  " and " + str(upper_limit) +  ": "))
count = 1
# While the user's guess does not equal the target value
while guess != target:
	# Report whether the guess was too big or too small
	if guess > target:
		print("That's too big!")
		upper_limit = guess - 1
	else:
		print("That's too small!")
		lower_limit = guess + 1

	# Count that a guess was made
	count = count + 1

	# Read another guess from the user
	guess = int(input("Enter a guess between " + str(lower_limit) +  " and " + str(upper_limit) +  ": "))
	while guess < lower_limit or guess > upper_limit:
		print("That wasn't a valid guess. Try again...")
		guess = int(input("Enter a guess between " + str(lower_limit) +  " and " + str(upper_limit) +  ": "))

# Disply result
print("That is the correct answer! It only took you", count, "guesses!")
