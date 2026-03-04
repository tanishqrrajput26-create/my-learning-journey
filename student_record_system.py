 # Dictionary to store student data
# Key = student name
# Value = student marks
students = {}

# Function to add a new student
def add_student():
    # Take student name as input
    name = input("Enter student name: ")
    
    # Take marks and convert into integer
    marks = int(input("Enter marks: "))
    
    # Store data in dictionary
    students[name] = marks
    
    print("Student added successfully!\n")


# Function to view all students
def view_students():
    # Check if dictionary is empty
    if not students:
        print("No student records found.\n")
    else:
        # Loop through dictionary items
        for name, marks in students.items():
            print(f"{name} : {marks}")
        print()


# Main function controls the program
def main():
    # Infinite loop to keep program running
    while True:
        # Display menu options
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")

        # Take user choice
        choice = input("Enter your choice: ")

        # Call function based on user choice
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            print("Exiting program...")
            break   # Stop the loop
        else:
            print("Invalid choice\n")


# Start the program
main()
