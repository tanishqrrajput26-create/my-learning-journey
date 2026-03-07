# Program to find the largest of three numbers

def find_largest(a, b, c):
    return max(a, b, c)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

largest = find_largest(num1, num2, num3)

print(f"The largest number is {largest}")
