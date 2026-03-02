# Simple Marks Calculator

name = input("Enter student name: ")

marks1 = int(input("Enter marks for Subject 1: "))
marks2 = int(input("Enter marks for Subject 2: "))
marks3 = int(input("Enter marks for Subject 3: "))

total = marks1 + marks2 + marks3
average = total / 3

print("\nStudent Name:", name)
print("Total Marks:", total)
print("Average Marks:", average)

if average >= 75:
    print("Grade: A")
elif average >= 50:
    print("Grade: B")
else:
    print("Grade: C")
