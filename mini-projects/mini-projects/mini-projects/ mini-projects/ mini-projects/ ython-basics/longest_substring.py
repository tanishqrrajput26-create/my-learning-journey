 # Longest Substring Without Repeating Characters

def longest_substring(s):
    char_set = set()
    left = 0
    max_length = 0
    longest = ""

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])

        # update max length
        if right - left + 1 > max_length:
            max_length = right - left + 1
            longest = s[left:right+1]

    return longest, max_length


# Input
text = input("Enter a string: ")

substring, length = longest_substring(text)

print("Longest substring:", substring)
print("Length:", length)


# Example Input:
# abcabcbb

# Example Output:
# Longest substring: abc
# Length: 3

# Input:
# pwwkew

# Output:
# Longest substring: wke
# Length: 3



#Imagine you are collecting unique chocolates 🍫

#Rules:

#You cannot take same chocolate twice
#If duplicate comes → throw old ones from left
 
