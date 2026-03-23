# Longest Palindrome Substring

def expand(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left+1:right]


def longest_palindrome(s):
    result = ""

    for i in range(len(s)):
        # Odd length
        p1 = expand(s, i, i)

        # Even length
        p2 = expand(s, i, i+1)

        # Take longer
        if len(p1) > len(result):
            result = p1
        if len(p2) > len(result):
            result = p2

    return result


# Input
text = input("Enter string: ")

print("Longest Palindrome:", longest_palindrome(text))

# Input:
# babad

# Output:
# bab
