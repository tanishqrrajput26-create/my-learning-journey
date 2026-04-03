# Rotate array by 1

arr = list(map(int, input("Enter elements: ").split()))

last = arr[-1]

for i in range(len(arr)-1, 0, -1):
    arr[i] = arr[i-1]

arr[0] = last

print("Rotated array:", arr)