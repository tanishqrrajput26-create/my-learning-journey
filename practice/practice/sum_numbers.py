# Program to add two numbers using a function

def add_numbers(a, b):
    return a + b

# Taking input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Calling function
result = add_numbers(num1, num2)

print(f"The sum of {num1} and {num2} is {result}")
