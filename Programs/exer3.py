# Converting human years to dog years more effectively

h_age = float(input("Enter an age in human years to convert to dog years: "))

# Display error message for values < 0
if h_age < 0:
	print("Please enter an age greater than 0.")

# Converting first two human years
elif h_age <= 2:
	d_age = h_age * 10.5
	print("The age of", h_age, 
		"in human years, is equivalent to", d_age, "in dog years") 

# Converting post-first two human years
else:
	h_age2 = h_age - 2
	d_age = (h_age2 * 4) + 21
	print("The age of", h_age, 
		"in human years, is equivalent to", d_age, "in dog years") 
