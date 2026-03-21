# Expense Tracker

expenses = []

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter amount: "))
        category = input("Enter category (food/travel/etc): ")
        
        expenses.append((amount, category))
        print("Expense added successfully!")

    elif choice == "2":
        print("\nAll Expenses:")
        for exp in expenses:
            print("Amount:", exp[0], "| Category:", exp[1])

    elif choice == "3":
        total = sum(exp[0] for exp in expenses)
        print("Total Expense:", total)

    elif choice == "4":
        break

    else:
        print("Invalid choice")


# Example:
# Input: 1 → 200 → food
# Output: Expense added successfully!
