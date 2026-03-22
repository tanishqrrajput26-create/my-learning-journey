# Zigzag Conversion

def zigzag_convert(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s

    rows = [""] * numRows
    current_row = 0
    going_down = False

    for char in s:
        rows[current_row] += char

        # Change direction
        if current_row == 0 or current_row == numRows - 1:
            going_down = not going_down

        # Move up or down
        if going_down:
            current_row += 1
        else:
            current_row -= 1

    return "".join(rows)


# Input
text = input("Enter string: ")
rows = int(input("Enter number of rows: "))

result = zigzag_convert(text, rows)

print("Zigzag Output:", result)

## Example Input:
# PAYPALISHIRING
# 3

# Output:
# PAHNAPLSIIGYIR
