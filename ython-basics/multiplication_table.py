 # Program to print multiplication table

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# Example Input:
# 5

# Example Output:
# 5 x 1 = 5
# 5 x 2 = 10
# ...
# 5 x 10 = 50