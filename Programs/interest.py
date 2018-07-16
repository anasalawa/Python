# A program that computes the payment amount 
# and total cost of borrowing for a loan

#Read input from the user
amount = float(input("How much is being borrowed? "))
rate = float(input("What's the interest rate percent? "))
years = int(input("How many years will it take to repay the loan? "))

#Compute the payment amount and the total cost of borrowing
num_payments = years * 12
rate = rate / 100 / 12

payment = rate * amount / (1 - (1 + rate) ** -num_payments)
cost = num_payments * payment - amount

#Display the results
print("The monthly payment is", payment)
print("The total cost of borrowing is", cost)
