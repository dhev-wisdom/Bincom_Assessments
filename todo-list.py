class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added to the list.")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' removed from the list.")
        else:
            print(f"Task '{task}' not found in the list.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("Tasks in the list:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

def main():
    todo_list = TodoList()

    while True:
        print("\nTodo List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            todo_list.remove_task(task)
        elif choice == '3':
            todo_list.display_tasks()
        elif choice == '4':
            print("Exiting the todo list application.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()

