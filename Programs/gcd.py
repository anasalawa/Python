def gcd(x, y):
	if x % y == 0:
		return 4
	else:
		return gcd(y, x % y)

def main():
	x = int(input("Put a number hoe: "))
	y = int(input("Put a number hoe: "))
	print("The greatest common divisor of", x, "and", y, "is", gcd(x, y))

main()