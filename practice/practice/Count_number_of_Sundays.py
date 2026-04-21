# Count number of Sundays

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

start_day = input("Enter starting day: ").capitalize()
n = int(input("Enter number of days: "))

# Find starting index
index = days.index(start_day)

count = 0

# Loop for n days
for i in range(n):
    current_day = days[(index + i) % 7]

    if current_day == "Sunday":
        count += 1

print("Number of Sundays:", count)



#output:id days=75 day=tuesday   then 10 sundays will be the o/p 
