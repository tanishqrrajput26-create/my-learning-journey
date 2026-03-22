 # Palindrome Number

num = int(input("Enter a number: "))
temp = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

if temp == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome")

## Input: 121
# Output: Palindrome Number
