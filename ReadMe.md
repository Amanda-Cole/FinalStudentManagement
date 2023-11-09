# Overview

Practice using SQL to connect and query a database through Python code.

I wrote a simple program that acts as a Student Management program.  Data is stored in a database through SQL workbench.  Through python, functions are called that then run queries to produce the desired information.  Functions to display, add, edit, delete, and see information through joined tables are included.

By writing this program I was able to learn and understand the ability for databases to be accessed through other code languages.  This knowledge will be benefitial moving forward and understanding large and complex programs that use databases.


[Student Management Video](https://youtu.be/S-myMbv8NFk)

# Relational Database

I used a database that I created in SQL Workbench. The database consists of three tables - students, counselors, and students_has_counselor.

The students table has the following setup:  

    students_id - int, Auto Incremented, Primary Key  
    first_name - VARCHAR(45)  
    last_name - VARCHAR (45)  
    grade - int  
    gpa - double

The counselors table has the following setup:  

    counselor_id - int, Auto Incremented, Primary Key  
    first_name - VARCHAR(45)  
    last_name - VARCHAR(45)
    spec_grade - int  

The students_has_counselor table has the following setup:  

    students_id - int Primary Key
    counselor_id - int Primary Key  

The students table is joined to the counselors table through the students_has_counselor table.  This is due to the fact that there is a many to many relationship.



# Development Environment

I used MySQL workbench and mySql.Connector to develop this software.

I used Python in Visual Studio Code to write this program.

# Useful Websites


- [Python MySQL Tutorial - Setup & Basic Queries (w/ MySQL Connector)](https://www.youtube.com/watch?v=3vsC05rxZ8c)
- [How to Run SQLITE in Visual Studio Code](https://www.youtube.com/watch?v=JrAiefGNUq8)
- [How to Use VS Code to Run SQL on a Database](https://www.youtube.com/watch?v=C0y35FpiLRA)




# Future Work


In the future I need to remember the following:
- Focus research on the basics and not get distracted by additional add-ons until the basics are solid.  

- Take time to practice the basics that relate to the purpose of my program.  

- Take notes with links to websites so resources can be found at later times in the build.