# Move zeros to end

arr = list(map(int, input("Enter elements: ").split()))

k = 0

# Move non-zero elements forward
for i in range(len(arr)):
    if arr[i] != 0:
        arr[k] = arr[i]
        k += 1

# Fill remaining with 0
for i in range(k, len(arr)):
    arr[i] = 0

print("Result:", arr)