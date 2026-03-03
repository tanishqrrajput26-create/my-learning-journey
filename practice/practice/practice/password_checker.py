# Simple Password Checker

password = input("Enter password: ")

if len(password) >= 6:
    print("Password length is valid")
else:
    print("Password too short")

if password.isdigit():
    print("Password should not be only numbers")
