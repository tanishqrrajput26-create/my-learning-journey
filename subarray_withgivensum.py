#Find subarray whose sum = target

Logic (Sliding Window)
Expand window → increase sum Shrink window → reduce sum

# Subarray with given sum


arr = list(map(int, input("Enter elements: ").split()))
target = int(input("Enter target sum: "))


#Input:
#1 2 3 7 5
#12

#Output:
#Subarray found from index 1 to 3


left = 0
current_sum = 0

for right in range(len(arr)):
    current_sum += arr[right]

    while current_sum > target:
        current_sum -= arr[left]
        left += 1

    if current_sum == target:
        print("Subarray found from index", left, "to", right)
        break
else:
    print("No subarray found")