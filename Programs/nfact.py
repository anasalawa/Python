# Compute n-factorial using a while loop

# Read n from the user
n = int(input("Enter a non-negative integer: "))
original_n = n
result = 1

# Compute n-factorial
while n > 0:
	result = result * n
	n = n - 1

# Display the result
print(original_n, "factorial is:", result)