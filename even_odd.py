 # Program to check whether a number is even or odd

# Take number input from user
num = int(input("Enter a number: "))

# Check if number is divisible by 2
if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")



# Function to check even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter a number: "))
result = check_even_odd(num)

print("The number is:", result)