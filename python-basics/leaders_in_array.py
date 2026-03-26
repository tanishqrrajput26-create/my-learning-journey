# Leaders in an Array

arr = list(map(int, input("Enter array elements: ").split()))

leaders = []
max_from_right = float('-inf')

# Traverse from right
for num in reversed(arr):
    if num >= max_from_right:
        leaders.append(num)
        max_from_right = num

# Reverse to correct order
leaders.reverse()

print("Leaders:", leaders)

# Input:
# 16 17 4 3 5 2

# Output:
# Leaders: [17, 5, 2]
