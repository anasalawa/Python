# Rewriting the factorial program using for loops

# Read n from the user
n = int(input("Enter a non-negative number: "))


# Compute n-factorial
result = 1
for i in range(1, n + 1):
	result = result * i

# Display the result
print(n, "factorial is", result)