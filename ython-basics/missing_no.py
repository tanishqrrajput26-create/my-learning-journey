# Find missing number

arr = list(map(int, input("Enter elements: ").split()))
n = len(arr) + 1

total = n * (n + 1) // 2
missing = total - sum(arr)

print("Missing number:", missing)