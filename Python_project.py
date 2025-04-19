import datetime

# List to store student data
students = []

# Function to add a student
def add_student():
    name = input("Enter the student's name: ")
    roll_number = input("Enter the student's roll number: ")
    due_date_str = input("Enter the fee due date (YYYY-MM-DD): ")
    tuition_fee = input("Enter the tuition fee amount: ")

    try:
        due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format! Use YYYY-MM-DD.\n")
        return

    # Check if roll number already exists
    for student in students:
        if student['roll_number'] == roll_number:
            print("Roll number already exists!\n")
            return

    student = {
        'name': name,
        'roll_number': roll_number,
        'fee_status': "unpaid",
        'due_date': due_date,
        'tuition_fee': tuition_fee
    }

    students.append(student)
    print(f"Student {name} added successfully.\n")

# Function to mark fee as paid
def mark_fee_paid():
    roll_number = input("Enter the roll number of the student to mark fee as paid: ")
    for student in students:
        if student['roll_number'] == roll_number:
            student['fee_status'] = 'paid'
            print(f"Fee marked as paid for {student['name']}.\n")
            return
    print("Student not found!\n")

# Function to send notifications for overdue fees
def send_notifications():
    today = datetime.datetime.today()
    for student in students:
        if student['fee_status'] == 'unpaid' and student['due_date'] < today:
            print(f"Notification: {student['name']} ({student['roll_number']}) has overdue fees! "
                  f"Due Date: {student['due_date'].strftime('%Y-%m-%d')}, "
                  f"Amount: ₹{student['tuition_fee']}\n")

# Function to display all students
def display_students():
    if not students:
        print("No students to display.\n")
        return
    for student in students:
        print(f"Name: {student['name']}, Roll No: {student['roll_number']}, "
              f"Fee Status: {student['fee_status']}, Due Date: {student['due_date'].strftime('%Y-%m-%d')}, "
              f"Tuition Fee: ₹{student['tuition_fee']}")
    print("\n")
 
 
def main():
    while True:
        print("Fee Notification System")
        print("1. Add Student")
        print("2. Mark Fee Paid")
        print("3. Send Fee Overdue Notifications")
        print("4. Display All Students")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            mark_fee_paid()
        elif choice == "3":
            send_notifications()
        elif choice == "4":
            display_students()
        elif choice == "5":
            print("Exiting system.")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()



 