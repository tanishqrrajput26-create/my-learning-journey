# Majority element

arr = list(map(int, input("Enter elements: ").split()))

count = 0
candidate = None

for num in arr:
    if count == 0:
        candidate = num
    count += (1 if num == candidate else -1)

print("Majority element:", candidate)