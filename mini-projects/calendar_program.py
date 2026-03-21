 # Calendar Program

import calendar

year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))

cal = calendar.month(year, month)

print("\nHere is the calendar:\n")
print(calendar.calendar(year))
print(cal)

# Example Input:
# 2026
# 3

# Example Output:
#     March 2026
# Mo Tu We Th Fr Sa Su
#                   1
#  2  3  4  5  6  7  8
#  9 10 11 12 13 14 15
# 16 17 18 19 20 21 22
# 23 24 25 26 27 28 29
# 30 31
