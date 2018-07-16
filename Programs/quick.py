a = float(input("Enter a float: "))
b = float(input("Enter another float: "))

print("a - b is %.25f" % (a - b))

if abs(a - b - 0.61) < 0.00000000001:
	print("The difference is 61 cents")
else:
	print("The difference is ****NOT**** 61 cents")