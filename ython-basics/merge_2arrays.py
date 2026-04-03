# Merge two arrays

arr1 = list(map(int, input("Enter first array: ").split()))
arr2 = list(map(int, input("Enter second array: ").split()))

merged = arr1 + arr2

print("Merged array:", merged)


#Input:
#1 2 3
#4 5 6

#Output:
#[1, 2, 3, 4, 5, 6]