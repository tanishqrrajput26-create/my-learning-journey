# Program to count vowels in a string

text = input("Enter a sentence: ")

vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Number of vowels:", count)


#Example Input:
# hello

# Example Output:
# Number of vowels: 2


