class Task:
    def __init__(self, id, title, description, priority, status):
        self.id = id
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status

    def __str__(self):
        return f"Task(ID: {self.id}, Title: {self.title}, Description: {self.description}, Priority: {self.priority}, Status: {self.status})"


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title, description, priority, status):
        task = Task(self.next_id, title, description, priority, status)
        self.tasks.append(task)
        self.next_id += 1
        print(f"Task added: {task}")

    def edit_task(self, task_id, title=None, description=None, priority=None, status=None):
        task = self.get_task_by_id(task_id)
        if task:
            if title:
                task.title = title
            if description:
                task.description = description
            if priority:
                task.priority = priority
            if status:
                task.status = status
            print(f"Task updated: {task}")
        else:
            print("Error: Task ID not found. Please enter a valid task ID.")

    def delete_task(self, task_id):
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            print(f"Task deleted: {task}")
        else:
            print("Error: Task ID not found. Please enter a valid task ID.")

    def get_task_by_id(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def view_all_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        for task in self.tasks:
            print(task)

    def filter_tasks_by_priority(self, priority):
        filtered_tasks = [task for task in self.tasks if task.priority == priority]
        if not filtered_tasks:
            print(f"No tasks found with priority: {priority}")
        for task in filtered_tasks:
            print(task)


def display_menu():
    print("\nTask Manager Menu")
    print("1. Add Task")
    print("2. Edit Task")
    print("3. Delete Task")
    print("4. View All Tasks")
    print("5. Filter Tasks by Priority")
    print("6. Exit")
    return input("Enter your choice: ")


def main():
    task_manager = TaskManager()
    while True:
        choice = display_menu()
        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            priority = input("Enter task priority (High/Medium/Low): ")
            status = input("Enter task status (Pending/In Progress/Completed): ")
            task_manager.add_task(title, description, priority, status)
        elif choice == '2':
            task_id = int(input("Enter task ID to edit: "))
            title = input("Enter new title (or press Enter to skip): ")
            description = input("Enter new description (or press Enter to skip): ")
            priority = input("Enter new priority (High/Medium/Low) (or press Enter to skip): ")
            status = input("Enter new status (Pending/In Progress/Completed) (or press Enter to skip): ")
            task_manager.edit_task(task_id, title, description, priority, status)
        elif choice == '3':
            task_id = int(input("Enter task ID to delete: "))
            task_manager.delete_task(task_id)
        elif choice == '4':
            task_manager.view_all_tasks()
        elif choice == '5':
            priority = input("Enter priority to filter by (High/Medium/Low): ")
            task_manager.filter_tasks_by_priority(priority)
        elif choice == '6':
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
