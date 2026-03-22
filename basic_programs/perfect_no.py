 # Perfect Number

num = int(input("Enter a number: "))
sum = 0

for i in range(1, num):
    if num % i == 0:
        sum += i

if sum == num:
    print("Perfect Number")
else:
    print("Not a Perfect Number")

#6 → 1 + 2 + 3 = 6 ✅
# Input: 6
# Output: Perfect Number
