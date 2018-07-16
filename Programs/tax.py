# Compute the amount of federal income tax payable without considering any
# deductions.

LIMIT_1 = 43561
LIMIT_2 = 87123
LIMIT_3 = 135054
LIMIT_4 = 200000

RATE_1 = 0.15
RATE_2 = 0.22
RATE_3 = 0.26
RATE_4 = 0.29
RATE_5 = 0.33

# Read income from the user
income = float(input("Enter the income: "))

if income < LIMIT_1:
	tax = RATE_1 * income
elif income < LIMIT_2:
	tax = RATE_1 * LIMIT_1 + RATE_2 * (income - LIMIT_1)
elif income < LIMIT_3:
	tax = RATE_1 * LIMIT_1 + RATE_2 * (income - LIMIT_1) + \
		  RATE_3 * (income - LIMIT_2)
elif income < LIMIT_4:
	tax = RATE_1 * LIMIT_1 + RATE_2 * (income - LIMIT_1) + \
		  RATE_3 * (income - LIMIT_2) + RATE_4 * (LIMIT_4 - LIMIT_3)
else:
	tax = RATE_1 * LIMIT_1 + RATE_2 * (income - LIMIT_1) + \
		  RATE_3 * (income - LIMIT_2) + RATE_4 * (LIMIT_4 - LIMIT_3) + \
		  RATE_5 * (income - LIMIT_4)

# Display the results
print("On an income of $" + format(income, ",.2f"),
	  "the income tax payable is $" + format(tax, ",.2f") + ".")
