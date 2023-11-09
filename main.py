import mysql.connector


#connection to mysql workbench database
connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Austin25$",
        database="sprint4_students"
    )
# Create a cursor object using the connection
cursor = connection.cursor()

# Function to display data from a table
def display_data():
    print("------------------------------------------------------")
    query = "SELECT * FROM students"
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        print(row)
    print("------------------------------------------------------")
    
# Function to add data to a table
def add_data():
    print("Enter data to add:")
    first_name = input("Enter value for First Name: ")
    last_name = input("Enter value for Last Name: ")
    grade = input("Enter value for Grade: ")
    gpa = input("Enter value for GPA: ")

    query = "INSERT INTO students (first_name, last_name, grade, gpa) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (first_name, last_name, grade, gpa))
    connection.commit()
    print()
    display_data()
    print()
    print("Data added successfully")

# Function to edit data in a table
def edit_data(edit_id):
    select_query = "SELECT first_name, last_name, grade, gpa FROM students WHERE students_id = %s"
    cursor.execute(select_query,(edit_id,))
    result = cursor.fetchall()
    for row in result:
        print(row)
    print()
    print("Enter your Updates:")
    new_firstname = input("Enter new value for First Name: ")
    new_lastname = input("Enter new value for Last Name: ")
    new_grade = input("Enter new value for Grade: ")
    new_gpa = input("Enter new value for GPA: ")


    query = "UPDATE students SET first_name = %s, last_name = %s, grade = %s , gpa = %s WHERE students_id = %s"
    cursor.execute(query, (new_firstname, new_lastname, new_grade, new_gpa, edit_id))
    connection.commit()
    print()
    display_data()
    print()
    print("Data updated successfully")

# Function to delete data from a table
def delete_data(delete_id):
    query = "DELETE FROM students WHERE students_id = %s"
    cursor.execute(query, (delete_id,))
    connection.commit()
    print()
    display_data()
    print("Data deleted successfully")
    
#function to return counselor for selected student
def retrieve_counselor():
    display_data()
    choice_id = input("Which student id are you searching for? ")
    query = """
        SELECT c.first_name, c.last_name
        FROM counselor c
        JOIN students_has_counselor shc ON c.counselor_id = shc.counselor_id
        JOIN students s ON s.students_id = shc.students_id
        WHERE s.students_id = %s
    """
    cursor.execute(query, (choice_id,))
    result = cursor.fetchall()

    if not result:
        print("No counselor found for the given student ID.")
    else:
        print("Counselor Information:")
        for row in result:
            print(row)



# Function to show menu options
def menu():
    while True:
        print("\nMenu:")
        print("1. Display data")
        print("2. Add data")
        print("3. Edit data")
        print("4. Delete data")
        print("5. Find Counselor")
        print("6. Exit")
        print()
        choice = input("Enter your choice (1-5): ")
        print()
        if choice == "1":
            print()
            print("Displaying data:")
            display_data()
        elif choice == "2":
            add_data()
        elif choice == "3":
            display_data()
            print()
            edit_id = input ("What student id would you like to edit?")
            edit_data(edit_id)
        elif choice == "4":
            display_data()
            print()
            delete_id = input ("What student id would you like to delete?")
            delete_data(delete_id)
        elif choice == "5":
            print()
            print("Get Counselor")
            retrieve_counselor()

        elif choice == "6":
            break
        else:
            print("Invalid choice. Please enter a valid option.")

# Run the menu
print("\033[1;31;40m Student Management System \033[0m")
menu()
# Close the cursor and the connection
cursor.close()
connection.close()    

