def read_tasks(filename):
    try:
        with open(filename, 'r') as file:
            tasks = [line.strip() for line in file]
            return tasks
    except FileNotFoundError:
        print(f"File '{filename}' not found. Creating a new task list.")
        return []

def write_tasks(filename, tasks):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(task + "\n")
        print("Task list saved successfully!")

def add_task(tasks):
    new_task = input("Enter a new task: ")
    tasks.append(new_task)
    print("Task added successfully!")

def remove_task(tasks):
    task_to_remove = input("Enter the task to remove: ")
    if task_to_remove in tasks:
        tasks.remove(task_to_remove)
        print("Task removed successfully!")
    else:
        print("Task not found in the list.")

def view_tasks(tasks):
    if tasks:
        print("Current tasks:")
        for task in tasks:
            print(task)
    else:
        print("No tasks in the list.")

def main():
    task_filename = "my_tasks.txt"
    tasks = read_tasks(task_filename)

    while True:
        print("\n1. Add a task")
        print("2. Remove a task")
        print("3. View tasks")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            remove_task(tasks)
        elif choice == '3':
            view_tasks(tasks)
        elif choice == '4':
            write_tasks(task_filename, tasks)
            print("Exiting the task list manager. Have a productive day!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

main()
