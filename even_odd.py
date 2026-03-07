# Program to check whether a number is even or odd

# Function to check even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Taking input from user
num = int(input("Enter a number: "))

# Calling the function
result = check_even_odd(num)

# Display result
print(f"The number {num} is {result}")
