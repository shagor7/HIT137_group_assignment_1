# Ask the user to enter a password
password = input("Please input your password: ")

# Counters for digits and uppercase letters
digit_count = 0
upper_count = 0

# Loop through each character in the password
for ch in password:
    # Check if the character is a digit (0-9)
    if '0' <= ch <= '9':
        digit_count += 1
    # Check if the character is an uppercase letter (A-Z)
    if 'A' <= ch <= 'Z':
        upper_count += 1

# Validate and classify the password strength
if len(password) < 6:
    print("Weak password")  # Password too short
elif len(password) <= 10:
    if digit_count >= 1:
        print("Medium password")  # Medium: 6-10 chars with at least 1 digit
    else:
        print("Weak password")  # No digit makes it weak
else:  # Password longer than 10 characters
    if digit_count >= 1 and upper_count >= 1:
        print("Strong password")  # Strong: long + at least 1 digit + 1 uppercase
    else:
        print("Medium password")  # Long but missing digit or uppercase → Medium