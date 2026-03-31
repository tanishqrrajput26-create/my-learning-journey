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

#Input:
#3 2 2 3 3

#Output:
#New length: 2
#Updated array: [2, 2]