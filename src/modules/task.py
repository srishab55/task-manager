class Task:
    task_id = 0
    task_name = ""
    task_description = ""
    task_status = ""
# This class represents a task with an ID, name, description, and status.
    def __init__(self,task_id, task_name, task_description,status="Pending"):
        self.task_id = task_id
        self.task_name = task_name
        self.task_description = task_description
        self.task_status = status

    def mark_completed(self):
        self.task_status = "Completed"

    def __str__(self):
        return f"{self.task_id}: {self.task_name} - {self.task_description}"
