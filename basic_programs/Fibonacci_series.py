# Fibonacci Series

n = int(input("Enter number of terms: "))

a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

 #input=5
# Output: 0 1 1 2 3
