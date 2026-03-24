# Container With Most Water

def max_area(height):
    left = 0
    right = len(height) - 1
    max_water = 0

    while left < right:
        width = right - left
        h = min(height[left], height[right])
        area = width * h

        max_water = max(max_water, area)

        # Move the smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water


# Input:
# 1 8 6 2 5 4 8 3 7

# Output:
# Maximum water: 49

#Area = min(height[left], height[right]) × width

# Input
heights = list(map(int, input("Enter heights (space separated): ").split()))

print("Maximum water:", max_area(heights))
