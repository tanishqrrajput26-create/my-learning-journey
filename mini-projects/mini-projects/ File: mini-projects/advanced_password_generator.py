# Advanced Password Generator

import random
import string

# Ask user for password length
length = int(input("Enter password length: "))

# All characters (letters + digits + symbols)
characters = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = ""

for i in range(length):
    password += random.choice(characters)

print("Generated Password:", password)

if length < 6:
    print("Password length should be at least 6")

# Example Input:
# 8

# Example Output:
# Generated Password: aB@9kL#2
