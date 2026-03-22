 # Armstrong Number Program

num = int(input("Enter a number: "))

# Count digits
power = len(str(num))

temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** power
    temp //= 10

if num == sum:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

# Example Input:
# 153

# Output:
# Armstrong Number
