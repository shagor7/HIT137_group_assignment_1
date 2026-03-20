# Password Input
password = input("Please Input Your Password: ")

if len(password) < 6: #check password length
    print("Weak password")
elif 6 <= len(password) <= 10 and any(char.isdigit() for char in password): #check password length and if it contains a number
    print("Medium password")
elif len(password) > 10 and any(char.isdigit() for char in password) and any(char.isupper() for char in password): #check password length and if it contains a number and an uppercase letter
    print("Strong Password")