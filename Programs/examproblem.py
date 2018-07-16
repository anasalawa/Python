# Figure whether a number is an abundant number
# Deficient number
# Perfect number

n = int(input("Enter an integer (0 or less to quit): "))

while n < 0:
	# Computing the total of the proper divisors
	total = 0
	for divisor in range(1, n): # Must be integer division because a for loop cannot return a floating point
		if n % divisor == 0:
			total = total + divisor

	# Reporting if the number is deficient, perfect, or abundant
	if total == n:
		print("That's a perfect number!")
	elif total < n:
		print("That's a deficient number!")
	else:
		print("That's an abundunt number!")





	n = int(input("Enter an integer (0 or less to quit): "))
	