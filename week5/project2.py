# Create an empty list to store tasks
tasks = []

# Add a task to the list
def add_task(task):
    tasks.append(task)
    print(f'Task "{task}" added!')

# Remove a task from the list
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f'Task "{task}" removed!')
    else:
        print("Task not found!")

# Show all tasks in the list
def view_tasks():
    if tasks:
        print("Your Tasks:")
        for number, task in enumerate(tasks, start=1):
            print(f"{number}. {task}")
    else:


        print("No tasks in your list!")

# Keep the program running until the user chooses to exit
while True:
    print("\nChoose an option:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        new_task = input("Enter the task: ")
        add_task(new_task)
    elif choice == '2':
        task_to_remove = input("Enter the task to remove: ")
        remove_task(task_to_remove)
    elif choice == '3':
        view_tasks()
    elif choice == '4':
        print("Goodbye! Stay organized!")
        break
    else:
        print("Invalid choice. Please try again.")


