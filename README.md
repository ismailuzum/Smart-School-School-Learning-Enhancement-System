Student Registration Project
-------------------------
This project has been developed using Python programming language and PyQt5 library, culminating in an executable application. The application allows users to register or log in using their email and password.
This project has been developed based on OOP, GUI, PostgreSQL, UML Diagrams and ERD Diagrams, culminating in an executable application. 
The application allows users to register or log in using their email and password.

User Types
--
The project encompasses the following three primary user types:

1. Admin

When logging into the application, the admin is recognized and directed to the admin panel. Here, the admin can create teacher accounts and make modifications to these accounts.
When the admin login, admin will reach the admin page.
Admin should be able to run all the functions.
Admin should approve/reject the new account requested by the teacher.

2. Teacher

Users logged in as teachers can access the teacher interface and perform functionalities as indicated in the diagram.
When the teachers login, they will reach the Teacher Page.
Every teacher has a profile page contains their own information.
Teachers can create, edit and view the annual course schedule.

3. Student

Students can log in or create a new account. These users can modify their own personal to-do lists. Additionally, they have access to information created by their teachers.
When the students login, they will reach the Student Page.
They can edit their own informations.
Students can view the annual course schedule (except for the teacher of those lessons)

Features
--------
-Each email address must be unique.

-Passwords should be eight characters long and include special characters.

-User data is stored in a JSON file.

![project uml diagram](Use_Case_diagram_SmartSchool.jpg)
-In the end, there should be a program that a user can run the program on Windows.

-To complete the project, all the members have to show up in the presentation and present the program.


