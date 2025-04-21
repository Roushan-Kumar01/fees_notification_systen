import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from datetime import datetime
import json

# List to store student data
students = []

# Function to add a student
def add_student():
    name = name_entry.get()
    roll_number = roll_entry.get()
    due_date_str = due_entry.get()
    tuition_fee = fee_entry.get()

    try:
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
    except ValueError:
        messagebox.showerror("Error", "Invalid date format! Use YYYY-MM-DD.")
        return

    for student in students:
        if student['roll_number'] == roll_number:
            messagebox.showerror("Error", "Roll number already exists!")
            return

    student = {
        'name': name,
        'roll_number': roll_number,
        'fee_status': "unpaid",
        'due_date': due_date,
        'tuition_fee': tuition_fee
    }

    students.append(student)
    messagebox.showinfo("Success", f"Student {name} added successfully.")
    clear_entries()

# Function to clear input fields
def clear_entries():
    name_entry.delete(0, tk.END)
    roll_entry.delete(0, tk.END)
    due_entry.delete(0, tk.END)
    fee_entry.delete(0, tk.END)

# Function to mark fee as paid
def mark_fee_paid():
    roll_number = roll_entry.get()
    for student in students:
        if student['roll_number'] == roll_number:
            student['fee_status'] = 'paid'
            messagebox.showinfo("Success", f"Fee marked as paid for {student['name']}.")
            return
    messagebox.showerror("Error", "Student not found!")

# Function to send overdue notifications
def send_notifications():
    today = datetime.today()
    notifications = ""
    for student in students:
        if student['fee_status'] == 'unpaid' and student['due_date'] < today:
            notifications += (f"{student['name']} ({student['roll_number']}) - Due: {student['due_date'].strftime('%Y-%m-%d')} - Amount: ₹{student['tuition_fee']}\n")

    if notifications:
        messagebox.showinfo("Overdue Fees", notifications)
    else:
        messagebox.showinfo("Overdue Fees", "No overdue fees found.")

# Function to display students
def display_students():
    display_win = tk.Toplevel(root)
    display_win.title("All Students")
    text = tk.Text(display_win, width=80, height=20)
    text.pack()
    if not students:
        text.insert(tk.END, "No students to display.\n")
    else:
        for student in students:
            text.insert(tk.END, f"Name: {student['name']}, Roll No: {student['roll_number']}, Fee Status: {student['fee_status']}, Due Date: {student['due_date'].strftime('%Y-%m-%d')}, Tuition Fee: ₹{student['tuition_fee']}\n")

# Function to search a student by roll number
def search_student():
    roll_number = roll_entry.get()
    for student in students:
        if student['roll_number'] == roll_number:
            messagebox.showinfo("Student Found", f"Name: {student['name']}, Roll No: {student['roll_number']}, Fee Status: {student['fee_status']}, Due Date: {student['due_date'].strftime('%Y-%m-%d')}, Tuition Fee: ₹{student['tuition_fee']}")
            return
    messagebox.showerror("Error", "Student not found!")

# Function to save student data to a file
def save_to_file():
    with filedialog.asksaveasfile(defaultextension=".json", filetypes=[("JSON Files", "*.json")]) as file:
        if file:
            json.dump(students, file)
            messagebox.showinfo("Success", "Data saved successfully.")

# Function to load student data from a file
def load_from_file():
    global students
    file_path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
    if file_path:
        with open(file_path, "r") as file:
            students = json.load(file)
        messagebox.showinfo("Success", "Data loaded successfully.")

# GUI Setup
root = tk.Tk()
root.title("Student Fee Management")

# Input Labels and Fields
tk.Label(root, text="Student Name").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Roll Number").grid(row=1, column=0, padx=10, pady=5)
roll_entry = tk.Entry(root)
roll_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Fee Due Date (YYYY-MM-DD)").grid(row=2, column=0, padx=10, pady=5)
due_entry = tk.Entry(root)
due_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Tuition Fee").grid(row=3, column=0, padx=10, pady=5)
fee_entry = tk.Entry(root)
fee_entry.grid(row=3, column=1, padx=10, pady=5)

# Buttons
tk.Button(root, text="Add Student", command=add_student).grid(row=4, column=0, padx=10, pady=10)
tk.Button(root, text="Mark Fee Paid", command=mark_fee_paid).grid(row=4, column=1, padx=10, pady=10)
tk.Button(root, text="Send Notifications", command=send_notifications).grid(row=5, column=0, padx=10, pady=10)
tk.Button(root, text="Display Students", command=display_students).grid(row=5, column=1, padx=10, pady=10)
tk.Button(root, text="Search Student", command=search_student).grid(row=6, column=0, padx=10, pady=10)
tk.Button(root, text="Save Data", command=save_to_file).grid(row=6, column=1, padx=10, pady=10)
tk.Button(root, text="Load Data", command=load_from_file).grid(row=7, column=0, padx=10, pady=10)
tk.Button(root, text="Exit", command=root.quit).grid(row=7, column=1, padx=10, pady=10)

root.mainloop()
