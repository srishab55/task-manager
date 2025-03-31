from services.task_manager import TaskManager
from modules.task import Task
from utils.db_utils import dbConnect # type: ignore
def main():
    manager = TaskManager()
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Print current Id")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            manager.add_task(title, description)
            print("Task added successfully.")
        elif choice == '2':
            manager.view_tasks()
        elif choice == '3':
            task_id = int(input("Enter task ID to mark as completed: "))
            if not manager.mark_task_completed(task_id):
                print(f"Task {task_id} not found.")
        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            manager.delete_task(task_id)
        elif choice == '5':
            manager.next_task_id = manager.getLatestTaskId()
            print(f"Current task ID: {manager.next_task_id}")
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
# This is a simple task manager program that allows users to add, view, mark as completed, and delete tasks.
# It uses a command-line interface for interaction.
