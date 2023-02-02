tasks = [] # List to store tasks

def print_menu():
    # Display the task manager menu options
    print("\nTask Manager\n")
    print("1. Add Task")
    print("2. Edit Task")
    print("3. Remove Task")
    print("4. List Tasks")
    print("5. Exit\n")

def add_task(task):
    # Add a new task to the list
    tasks.append(task)
    print(f"Task '{task}' added successfully")

def edit_task(task_index, new_task):
    # Edit an existing task
    tasks[task_index] = new_task
    print(f"Task '{tasks[task_index]}' edited successfully")

def remove_task(task_index):
    # Remove a task from the list
    task = tasks.pop(task_index)
    print(f"Task '{task}' removed successfully")

def list_tasks():
    # List all the tasks
    print("\nTask List\n")
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task}")

def main():
    # Main loop to display the menu and handle user input
    while True:
        print_menu()
        option = int(input("Select an option: "))

        if option == 1:
            task = input("Add a new task: ")
            add_task(task)
        elif option == 2:
            task_index = int(input("Select the task to edit: ")) - 1
            new_task = input("Enter the new task description: ")
            edit_task(task_index, new_task)
        elif option == 3:
            task_index = int(input("Select the task to remove: ")) - 1
            remove_task(task_index)
        elif option == 4:
            list_tasks()
        elif option == 5:
            break
        else:
            print("Invalid option, please select a valid option\n")

if __name__ == "__main__":
    main()
