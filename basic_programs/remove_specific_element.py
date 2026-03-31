# Remove a specific element

arr = list(map(int, input("Enter elements: ").split()))
x = int(input("Enter element to remove: "))

# Remove all occurrences
arr = [num for num in arr if num != x]

print("Updated list:", arr)