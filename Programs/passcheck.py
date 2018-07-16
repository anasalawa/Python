# Determine whether or not a password is "secure". A "secure" password is
#	At least 7 characters
#	Contains at least one uppercase letter
#	Contains at least one lowercase letter
#	Contains at least one numeric digit

#
# Returns: True if the password is "secure", False otherwise
#

def isSecure(password):
		# Verify the length of the password
	if len(password) < 7:
		return False
	
	# Verify the password contains an uppercase letter
	hasUpper = False
	for chU in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
		if password.find(chU) >= 0:
			hasUpper = True

	if hasUpper == False:
			return False

	# Verifiy that the password containts a lowercase letter
	hasLower = False
	for ch in password:
		if ch >= "a" and ch <= "z": # goes off based on ASCII
			hasLower = True

	if hasLower == False:
		return False

	# Verifiy that the password containts a digit
	hasDigit == False
	for d in "0123456789":
		if d in password:
			hasDigit == True

	if hasDigit == False:
		return False

	return True

def main():
	password = input("Enter a password: ")
	if isSecure(password) == True:
		print("That's a good, secure password.")
	if isSecure(password) == False:
		print(password, "is not a good, secure password.")

main()