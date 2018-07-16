# Compute n-factorial using recursion
def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n - 1)  # Calling the function within the function


def main():
	a = int(input("Enter a non negative int: "))
	print(a, "factorial is", factorial(a))

main()