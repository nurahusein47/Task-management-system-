Simple Task Management System

A Python-based command-line program that helps users organize and manage daily activities by adding, viewing, and deleting tasks easily.

Introduction

The Simple Task Management System is a Python program designed to help users organize and manage their daily activities. The program allows users to add tasks, view saved tasks, and delete tasks that are no longer needed.

This project was developed to practice fundamental programming concepts such as lists, loops, conditional statements, and user input handling. It provides a simple and practical solution for managing personal tasks.

Objectives

· To develop a task management system using Python
· To store and manage tasks using lists
· To allow users to add, view, and delete tasks
· To display the total number of tasks
· To improve programming and problem-solving skills

Features

· Users can add new tasks easily
· Tasks can be viewed in a simple list
· Existing tasks can be updated when needed
· Unwanted or completed tasks can be deleted
· Supports storing multiple tasks using lists
· Simple menu system makes it easy to use
· Handles invalid input to avoid errors

Tech Stack

· Python 3.x
· Command-line interface

Installation

1. Make sure Python 3 is installed on your system.
2. Save the code file as task_manager.py.
3. Run the script:
  
   python task_manager.py
   
Usage

1. Launch the program.
2. Choose from the menu options:
   · Add Task – Add one or more tasks (separated by commas)
   · View Tasks – See all saved tasks
   · Delete Task – Remove a task by its number
   · Exit – Close the program

Sample Output

Adding Multiple Tasks

--- TASK MANAGEMENT SYSTEM ---
1. Add Task
2. View Tasks
3. Delete Task
4. Exit
Enter your choice: 1
Enter task(s) separated by commas: Study Python, Complete Assignment, Read Book
Task(s) added successfully!
Viewing Tasks

--- TASK MANAGEMENT SYSTEM ---
1. Add Task
2. View Tasks
3. Delete Task
4. Exit
Enter your choice: 2

Your Tasks:
1. Study Python
2. Complete Assignment
3. Read Book
Total Tasks: 3
Deleting a Task

--- TASK MANAGEMENT SYSTEM ---
1. Add Task
2. View Tasks
3. Delete Task
4. Exit
Enter your choice: 3

1. Study Python
2. Complete Assignment
3. Read Book
Enter task number to delete: 2
Task 'Complete Assignment' deleted.

Updated Task List:
1. Study Python
2. Read Book
Total Tasks: 2
Concepts Used

· Variables
· Lists
· While loops
· For loops
· Conditional statements (if, elif, else)
· User input and output
· String methods (split() and strip())
· Built-in function (len())

Algorithm

1. Start the program
2. Create an empty list to store tasks
3. Display the task management menu
4. Show the total number of tasks
5. If user selects Add Task:
   · Enter one or more tasks separated by commas
   · Store each task in the list
6. If user selects View Tasks:
   · Display all saved tasks
7. If user selects Delete Task:
   · Display available tasks
   · Ask user to enter a task number
   · Delete the selected task
8. If user selects Exit: End the program
9. Stop

What I Learned

Through this project, I learned how to use Python lists to store and manage data efficiently. I also improved my understanding of loops, conditional statements, and string manipulation methods such as split() and strip(). In addition, I learned how to build a menu-driven program that allows users to interact with the system easily.

Future Improvements

· Add task priority levels
· Mark tasks as completed
· Save tasks permanently in a file
· Create graphical user interface (GUI)
· Add task search functionality

Conclusion
In this project, I successfully developed a Simple Task Management System using Python. The program allows users to add, view, and delete tasks while keeping track of the total number of tasks. This project strengthened my understanding of basic programming concepts and demonstrated how programming can be used to solve everyday problems.

About the Author

Nura Husein
Student / Beginner Python Developer

This project was developed as part of a learning exercise to strengthen programming fundamentals. Passionate about building small, useful tools and gradually moving into real-world applications.

· GitHub: nurahusein47(https://github.com/nurahusein47)
· Goal: Continue improving and building more interactive systems with databases and GUIs.

Acknowledgments

· Inspired by the need to organize daily tasks simply and effectively.
· Thanks to Python practice projects that helped build this system.

Version

v1.0 – Basic task management with add, view, and delete features (command-line based)

License

This project is for educational purposes only.
