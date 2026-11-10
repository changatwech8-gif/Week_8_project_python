
# STUDENT MINI MANAGEMENT TOOLKIT
# PLP PYTHON WEEK 8 PROJECT

# Welcome message
print("========================================")
print("       STUDENT MINI MANAGEMENT TOOLKIT")
print("========================================")
print("Welcome! Manage your student activities.")

# Keep showing the menu until the user chooses Quit
while True:

    print("\n1. Register a Student")
    print("2. Calculate Student Marks")
    print("3. View Student Records")
    print("4. Quit")

    choice = input("\nEnter your choice (1-4): ")

    if choice == "1":
        print("Student Registration selected.")

    elif choice == "2":
        print("Student Marks Calculator selected.")

    elif choice == "3":
        print("Student Records Viewer selected.")

    elif choice == "4":
        print("Thank you for using the Student Mini Management Toolkit. Goodbye!")
        break

    else:
        print(f"Sorry, {choice} is not a valid choice. Please select a number from 1 to 4.")
