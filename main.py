# # import tkinter as tk
# # import sqlite3
# # from tkinter import ttk, messagebox

# # root = tk.Tk()
# # root.title("Management")

# # connection = sqlite3.connect("sprint4_students.db")
# # cursor = connection.cursor()

# # TABLE_NAME = "students"
# # STUDENT_ID = "students_id"
# # FIRST_NAME = "first_name"
# # LAST_NAME = "last_name"
# # GRADE = "grade"
# # GPA = "gpa"

# # class Student:
# #     first_name = ""
# #     last_name = ""
# #     grade = ""
# #     gpa =""

# #     def __init__(self,first_name,last_name,grade,gpa):
# #         self.first_name = first_name
# #         self.last_name = last_name
# #         self.grade = grade
# #         self.gpa = gpa
        

# # #Build form basics
# # appLabel = tk.Label(root, text="Student Management System", fg = "#06a099", width = 35)
# # appLabel.config(font = ("Sylfaen",30))
# # appLabel.grid(row=0, columnspan=2, padx=(10,10), pady=(30,0))

# # #Create Labels for input
# # fnameLabel = tk.Label(root, text="Student First Name", width=40, anchor = 'w',
# #                      font = ("Sylfaen",12)).grid(row=1, column=0, padx=(10,0),
# #                      pady=(30,0))
# # lnameLabel = tk.Label(root, text="Student Last Name", width=40, anchor = 'w',
# #                      font = ("Sylfaen",12)).grid(row=2, column=0, padx=(10,0),
# #                      pady=(30,0))
# # gradeLabel = tk.Label(root, text="Student Grade", width=40, anchor = 'w',
# #                      font = ("Sylfaen",12)).grid(row=3, column=0, padx=(10,0),
# #                      pady=(30,0))
# # gpaLabel = tk.Label(root, text="Student GPA", width=40, anchor = 'w',
# #                      font = ("Sylfaen",12)).grid(row=4, column=0, padx=(10,0),
# #                      pady=(30,0))

# # #Create input boxes.  Grid shows place on form
# # fnameEntry = tk.Entry(root, width=30)
# # fnameEntry.grid(row=1, column=1,padx=(0,10),pady=(30,20))
# # lnameEntry = tk.Entry(root, width=30)
# # lnameEntry.grid(row=2, column=1,padx=(0,10),pady=(30,20))
# # gradeEntry = tk.Entry(root, width=30)
# # gradeEntry.grid(row=3, column=1,padx=(0,10),pady=(30,20))
# # gpaEntry = tk.Entry(root, width=30)
# # gpaEntry.grid(row=4, column=1,padx=(0,10),pady=(30,20))


# # def addStudentInput():
# #     # global fnameEntry, lnameEntry, gradeEntry, gpaEntry
# #     # global list
# #     # global TABLE_NAME, FIRST_NAME, LAST_NAME, GRADE, GPA
# #     firstname = fnameEntry.get()
# #     fnameEntry.delete(0, tk.END)
# #     lastname = lnameEntry.get()
# #     lnameEntry.delete(0,tk.END)
# #     grade = int(gradeEntry.get())
# #     gradeEntry.delete(0, tk.END)
# #     gpa = double(gpaEntry.get())
# #     gpaEntry.delete(0, tk.END)
    
    
# #     #INSERT INTO DATABASE
# #     connection = sqlite3.connect('sprint4_students.db')
# #     cursor = connection.cursor()
    
# #     cursor.execute(("INSERT INTO students (first_name, last_name, grade, gpa) VALUES (?, ?, ?, ?)",
# #                    (firstname, lastname, grade, gpa)))
    

# #     connection.commit()
# #     messagebox.showinfo("Success, Student Added")
 



# # button = tk.Button(root, text="Add Student", command=lambda :addStudentInput())
# # button.grid(row=5, column=0, pady=20)

# # # displayButton = tk.Button(root, text="Display Students", command=lamda : destroyRootWindow())
# # # displayButton.grid(row=5, column=1)





# # #Starts build
# # root.mainloop()

# import tkinter as tk
# from tkinter import messagebox
# import mysql.connector

# root = tk.Tk()
# root.title("Management")



# def create_connection():
#     return mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="Austin25$",
#         database="sprint4_students"
# )


# class Student:
#     def __init__(self, first_name, last_name, grade, gpa):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.grade = grade
#         self.gpa = gpa

# connection = create_connection()
# cursor = connection.cursor()     

# # Your Tkinter GUI code...
# # #Build form basics
# appLabel = tk.Label(root, text="Student Management System", fg = "#06a099", width = 35)
# appLabel.config(font = ("Sylfaen",30))
# appLabel.grid(row=0, columnspan=2, padx=(10,10), pady=(30,0))

# #Create Labels for input
# fnameLabel = tk.Label(root, text="Student First Name", width=40, anchor = 'w',
#                      font = ("Sylfaen",12)).grid(row=1, column=0, padx=(10,0),
#                      pady=(30,0))
# lnameLabel = tk.Label(root, text="Student Last Name", width=40, anchor = 'w',
#                      font = ("Sylfaen",12)).grid(row=2, column=0, padx=(10,0),
#                      pady=(30,0))
# gradeLabel = tk.Label(root, text="Student Grade", width=40, anchor = 'w',
#                      font = ("Sylfaen",12)).grid(row=3, column=0, padx=(10,0),
#                      pady=(30,0))
# gpaLabel = tk.Label(root, text="Student GPA", width=40, anchor = 'w',
#                      font = ("Sylfaen",12)).grid(row=4, column=0, padx=(10,0),
#                      pady=(30,0))

# #Create input boxes.  Grid shows place on form
# fnameEntry = tk.Entry(root, width=30)
# fnameEntry.grid(row=1, column=1,padx=(0,10),pady=(30,20))
# lnameEntry = tk.Entry(root, width=30)
# lnameEntry.grid(row=2, column=1,padx=(0,10),pady=(30,20))
# gradeEntry = tk.Entry(root, width=30)
# gradeEntry.grid(row=3, column=1,padx=(0,10),pady=(30,20))
# gpaEntry = tk.Entry(root, width=30)
# gpaEntry.grid(row=4, column=1,padx=(0,10),pady=(30,20))


# def addStudentInput():
#     try:
#         firstname = fnameEntry.get()
#         fnameEntry.delete(0, tk.END)
#         lastname = lnameEntry.get()
#         lnameEntry.delete(0, tk.END)
#         grade = int(gradeEntry.get())
#         gradeEntry.delete(0, tk.END)
#         gpa = float(gpaEntry.get())
#         gpaEntry.delete(0, tk.END)
        
#         # INSERT INTO DATABASE
#         insert_query = "INSERT INTO students (first_name, last_name, grade, gpa) VALUES (%s, %s, %s, %s)"
#         cursor.execute(insert_query, (firstname, lastname, grade, gpa))
#         connection.commit()
#         messagebox.showinfo("Success", "Student Added Successfully")
#     except ValueError:
#         messagebox.showerror("Error", "Invalid input. Please enter valid data.")
        
# def displayStudents():
#     try:
#         global cursor, connection  # Accessing the global cursor and connection

#         # Check if connection is closed, then re-establish the connection
#         if not connection.is_connected():
#             connection = create_connection()
#             cursor = connection.cursor()

#         select_query = "SELECT * FROM students"

#         cursor.execute(select_query)
#         students = cursor.fetchall()

#         display_window = tk.Toplevel(root)
#         display_window.title("Student Records")

#         if students:
#             for i, student in enumerate(students):
#                 student_info = f"ID: {student[0]}, Name: {student[1]} {student[2]}, Grade: {student[3]}, GPA: {student[4]}"
#                 label = tk.Label(display_window, text=student_info)
#                 label.grid(row=i, column=0, padx=10, pady=5)
#         else:
#             messagebox.showinfo("No Students", "No student records found.")
#     except mysql.connector.Error as e:
#         messagebox.showerror("Error", f"MySQL Error: {e}")

          
# try:
#     button = tk.Button(root, text="Add Student", command=addStudentInput)
#     button.grid(row=5, column=0, pady=20)
#     connection.commit()
# except mysql.connector.Error as error:
#     print("Failed to insert record into MySQL table:", error)
# finally:
#     if connection.is_connected():
#         cursor.close()
#         connection.close()
  
  
        
# try:
#     display_button = tk.Button(root, text="Display Students", command=displayStudents)
#     display_button.grid(row=6, column=0, pady=20)
#     connection.commit()
# except mysql.connector.Error as error:
#     print("Failed to display from MySQL table:", error)
# finally:
#     if connection.is_connected():
#         cursor.close()
#         connection.close()

# root.mainloop()
import tkinter as tk
import mysql.connector
from tkinter import messagebox

def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Austin25$",
        database="sprint4_students"
    )

def addStudentInput():
    try:
        firstname = fnameEntry.get()
        fnameEntry.delete(0, tk.END)
        lastname = lnameEntry.get()
        lnameEntry.delete(0, tk.END)
        grade = int(gradeEntry.get())
        gradeEntry.delete(0, tk.END)
        gpa = float(gpaEntry.get())
        gpaEntry.delete(0, tk.END)
        
        # INSERT INTO DATABASE
        insert_query = "INSERT INTO students (first_name, last_name, grade, gpa) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_query, (firstname, lastname, grade, gpa))
        connection.commit()
        messagebox.showinfo("Success", "Student Added Successfully")
    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

def displayStudents():
    try:
        global cursor, connection
        
        # Check if the connection is closed, then re-establish the connection
        if not connection.is_connected():
            connection = create_connection()
            cursor = connection.cursor()

        select_query = "SELECT * FROM students"
        cursor.execute(select_query)
        students = cursor.fetchall()

        display_window = tk.Toplevel(root)
        display_window.title("Student Records")

        if students:
            for i, student in enumerate(students):
                student_info = f"ID: {student[0]}, Name: {student[1]} {student[2]}, Grade: {student[3]}, GPA: {student[4]}"
                label = tk.Label(display_window, text=student_info)
                label.grid(row=i, column=0, padx=10, pady=5)
        else:
            messagebox.showinfo("No Students", "No student records found.")
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"MySQL Error: {e}")

# Initialize Tkinter window
root = tk.Tk()
root.title("Management")

# Establish initial database connection and cursor
connection = create_connection()
cursor = connection.cursor()

# Your Tkinter GUI code...
appLabel = tk.Label(root, text="Student Management System", fg="#06a099", width=35)
appLabel.config(font=("Sylfaen", 30))
appLabel.grid(row=0, columnspan=2, padx=(10, 10), pady=(30, 0))

fnameLabel = tk.Label(root, text="Student First Name", width=40, anchor='w', font=("Sylfaen", 12))
fnameLabel.grid(row=1, column=0, padx=(10, 0), pady=(30, 0))

lnameLabel = tk.Label(root, text="Student Last Name", width=40, anchor='w', font=("Sylfaen", 12))
lnameLabel.grid(row=2, column=0, padx=(10, 0), pady=(30, 0))

gradeLabel = tk.Label(root, text="Student Grade", width=40, anchor='w', font=("Sylfaen", 12))
gradeLabel.grid(row=3, column=0, padx=(10, 0), pady=(30, 0))

gpaLabel = tk.Label(root, text="Student GPA", width=40, anchor='w', font=("Sylfaen", 12))
gpaLabel.grid(row=4, column=0, padx=(10, 0), pady=(30, 0))

fnameEntry = tk.Entry(root, width=30)
fnameEntry.grid(row=1, column=1, padx=(0, 10), pady=(30, 20))

lnameEntry = tk.Entry(root, width=30)
lnameEntry.grid(row=2, column=1, padx=(0, 10), pady=(30, 20))

gradeEntry = tk.Entry(root, width=30)
gradeEntry.grid(row=3, column=1, padx=(0, 10), pady=(30, 20))

gpaEntry = tk.Entry(root, width=30)
gpaEntry.grid(row=4, column=1, padx=(0, 10), pady=(30, 20))

# Buttons to Add and Display students
button = tk.Button(root, text="Add Student", command=addStudentInput)
button.grid(row=5, column=0, pady=20)

display_button = tk.Button(root, text="Display Students", command=displayStudents)
display_button.grid(row=6, column=0, pady=20)

root.mainloop()
