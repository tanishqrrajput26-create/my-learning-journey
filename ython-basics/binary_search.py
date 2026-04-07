# Binary Search

arr = list(map(int, input("Enter sorted array: ").split()))
target = int(input("Enter number to search: "))

left = 0
right = len(arr) - 1

found = False

while left <= right:
    mid = (left + right) // 2

    if arr[mid] == target:
        print("Found at index:", mid)
        found = True
        break

    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

if not found:
    print("Not found")

#Input:
#1 3 5 7 9
#5

#Output:
#Found at index: 2