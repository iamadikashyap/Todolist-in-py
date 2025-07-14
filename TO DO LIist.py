todo_list = []

def show_menu():
    print("\n------ TODO List Menu ------")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    choice = get_choice()
    
    if choice == 1:
        add_tasks()
    elif choice == 2:
        view_tasks()
    elif choice == 3:
        remove_tasks()
    elif choice == 4:
        print("Exiting the TODO List.")
    else:
        print("Invalid choice.")
        show_menu()

def get_choice():
    try:
        return int(input("Enter your choice (1-4): "))
    except ValueError:
        print("Please enter a valid number.")
        return get_choice()

def add_tasks():
    add_task = input("Enter the task you want to add: ")
    todo_list.append(add_task)
    print(f"Task '{add_task}' has been added to the TODO list.")
    show_menu()

def view_tasks():
    if not todo_list:
        print("TODO List is empty.")
    else:
        print("\nYour TODO List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")
    show_menu()

def remove_tasks():
    if not todo_list:
        print("TODO List is empty.")
    else:
        print("\nSelect the task number to remove:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")
        try:
            task_number = int(input("Enter task number to remove: "))
            if 1 <= task_number <= len(todo_list):
                removed = todo_list.pop(task_number - 1)
                print(f"Removed task: {removed}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
    show_menu()

# Start the program
show_menu()
