def addStudentInput():
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
#     except ValueError as e:
#         messagebox.showerror("Error", f"Invalid input: {e}")
