tasks = []

while True:
    print("\n--- TASK MANAGEMENT SYSTEM ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task_input = input("Enter task(s) separated by commas: ")
        new_tasks = task_input.split(",")

        for task in new_tasks:
            tasks.append(task.strip())

        print("Task(s) added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")
            print("Total Tasks:", len(tasks))

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")

            num = int(input("Enter task number to delete: "))

            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"Task '{removed}' deleted.")
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Exiting Task Management System...")
        break

    else:
        print("Invalid choice. Please try again.")
