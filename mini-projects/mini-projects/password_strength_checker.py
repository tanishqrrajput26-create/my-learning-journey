# Password strength checker

password = input("Enter your password: ")

if len(password) < 6:
    print("Weak password")
elif len(password) < 10:
    print("Medium strength password")
else:
    print("Strong password")
