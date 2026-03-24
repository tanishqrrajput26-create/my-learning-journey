# Longest Substring with K Unique Characters

def longest_k_unique(s, k):
    left = 0
    max_length = 0
    char_count = {}

    for right in range(len(s)):
        # Add character
        char = s[right]
        char_count[char] = char_count.get(char, 0) + 1

        # If more than k unique → shrink window
        while len(char_count) > k:
            left_char = s[left]
            char_count[left_char] -= 1

            if char_count[left_char] == 0:
                del char_count[left_char]

            left += 1

        # Update max length
        if len(char_count) == k:
            max_length = max(max_length, right - left + 1)

    return max_length


# Input
s = input("Enter string: ")
k = int(input("Enter K: "))

print("Longest length:", longest_k_unique(s, k))
