tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        for i, task_info in enumerate(tasks, 1):
            task, done = task_info
            status = "✔️" if done else "❌"
            print(f"{i}. [{status}] {task}")

def add_task(task):
    tasks.append([task, False])
    print(f"Added: '{task}'")

def complete_task(index):
    if 0 <= index < len(tasks):
        tasks[index][1] = True
        print(f"Completed: '{tasks[index][0]}'")
    else:
        print("Invalid task number.")

def remove_task(index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"Removed: '{removed[0]}'")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nOptions: show / add / complete / remove / quit")
        action = input("Choose an action: ").strip().lower()

        if action == "show":
            show_tasks()
        elif action == "add":
            task = input("Enter task: ").strip()
            add_task(task)
        elif action == "complete":
            try:
                index = int(input("Enter task number to mark as complete: ")) - 1
                complete_task(index)
            except ValueError:
                print("Please enter a valid number.")
        elif action == "remove":
            try:
                index = int(input("Enter task number to remove: ")) - 1
                remove_task(index)
            except ValueError:
                print("Please enter a valid number.")
        elif action == "quit":
            print("Goodbye!")
            break
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()