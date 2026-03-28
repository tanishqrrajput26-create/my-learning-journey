# Butterfly Pattern

n = int(input("Enter size: "))

# Upper part
for i in range(1, n+1):
    print("*" * i, end="")
    print(" " * (2*(n-i)), end="")
    print("*" * i)

# Lower part
for i in range(n, 0, -1):
    print("*" * i, end="")
    print(" " * (2*(n-i)), end="")
    print("*" * i)