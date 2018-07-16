import math

def readFloat(prompt = ""):
	ve = False
	while ve == False:
		try:
			x = float(input("Enter a number: "))
			ve = True
		
		except ValueError:
			print("That wasn't a number. Try again.")

	return x


a = readFloat("Enter a number: ")
b = readFloat("Enter another number: ")

try:
	print(a, "+", b, "is", a + b)
	print(a, "-", b, "is", a - b)
	print(a, "*", b, "is", a * b)
	print(a, "/", b, "is", a / b)
	z = 1 + "asdf"

except ZeroDivisionError:
	print("Division by zero is not supported.")

except:
	print("Something went wrong!")
	quit()

try:
	print("sqrt(", a, ") is", math.sqrt(a))

except ValueError:
	print("The square root of negative numbers is not supported.")

print("The rest of the program.")

readFloat()

