# Program to check palindrome word

text = input("Enter a word: ")

if text == text[::-1]:
    print("The word is a palindrome")
else:
    print("The word is not a palindrome")
