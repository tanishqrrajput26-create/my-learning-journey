# Program to find sum of numbers from 1 to N

n = int(input("Enter a number: "))

total = 0

for i in range(1, n + 1):
    total += i

print("Sum of numbers from 1 to", n, "is:", total)