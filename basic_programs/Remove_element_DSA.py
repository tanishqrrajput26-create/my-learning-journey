# Remove element in-place

arr = list(map(int, input("Enter elements: ").split()))
x = int(input("Enter element to remove: "))

k = 0  # pointer

for i in range(len(arr)):
    if arr[i] != x:
        arr[k] = arr[i]
        k += 1

print("New length:", k)
print("Updated array:", arr[:k])