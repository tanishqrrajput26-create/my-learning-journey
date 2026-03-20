# Simple To-Do List

tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        for i, t in enumerate(tasks, 1):
            print(i, ".", t)

    elif choice == "3":
        break

    else:
        print("Invalid choice")
