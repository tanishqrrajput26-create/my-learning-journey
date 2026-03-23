# Two Sum
#Given numbers, find 2 numbers whose sum = target

nums = [2, 7, 11, 15]
target = 9

seen = {}

for i in range(len(nums)):
    diff = target - nums[i]

    if diff in seen:
        print("Indices:", seen[diff], i)
        break

    seen[nums[i]] = i
    

#nums = [2, 7, 11, 15]
#target = 9
#2 + 7 = 9 ✅
