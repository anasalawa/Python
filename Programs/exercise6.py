# Anas Alawa | 30016568 | L02 T11

# Write a program that can read a postal code and return the correct
# location.
# Creating the dictionary (prov = province)
prov = {"T": "Alberta", "V": "British Columbia", "R": "Manitoba",
		"E": "New Brunswick", "A": "Newfoundland", "B": "Nova Scotia",
		"X": "Nunavut or Northwest Territories", 
		"K": "Ontario", "L": "Ontario", "M": "Ontario", "N": "Ontario",
		"P": "Ontario", "G": "Quebec", "H": "Quebec", "J": "Quebec", 
		"C": "Prince Edward Island", "S": "Saskatchewan", "Y": "Yukon"}

# Read a postal code from a user (pcode = provincial code)
pcode = input("Enter a 6 character postal code (A1A1A1): ")

# Only need to consider the first letter
pcode = pcode[0]

# Print the correct province
print("That postal code resides in", prov[pcode.upper()])