 # Count elements greater than all previous elements

arr = list(map(int, input("Enter array elements: ").split()))

count = 0
max_so_far = float('-inf')

for num in arr:
    if num > max_so_far:
        count += 1
        max_so_far = num

print("Count:", count)
``
