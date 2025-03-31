from modules.task import Task
from utils.db_utils import dbConnect # type: ignore
from config import * # type: ignore


class TaskManager:
    """
    A simple task manager that allows users to add, view, mark as completed, and delete tasks."
    """
    next_task_id = 1
    def __init__(self):
        self.tasks = []
        self.next_task_id = 1
        connectorObj = dbConnect(DATABASE_NAME).connect()
        cursor = connectorObj.cursor()
        cursor.execute("SELECT max(task_id) FROM taskInformation")
        rows = cursor.fetchall()
        if rows[0][0] is not None:
            self.next_task_id = rows[0][0] + 1
        else:
            self.next_task_id = 1
        cursor.close() 
        connectorObj.close()
        

    def add_task(self, title, description):
        task = Task(self.next_task_id, title, description)
        self.tasks.append(task)
        print(f"Adding to database.")
        connectorObj = dbConnect(DATABASE_NAME).connect()
        cursor = connectorObj.cursor()
        sql = "INSERT INTO taskInformation (task_id, task_name, task_description, task_status) VALUES (%s, %s, %s, %s)"
        val = (task.task_id, task.task_name, task.task_description, task.task_status)
        cursor.execute(sql, val)
    
        connectorObj.commit()
        print(f"Task {task.task_id} added to database.")
        cursor.close()
        connectorObj.close()
        self.next_task_id += 1


    def view_tasks(self):
        connectorObj = dbConnect(DATABASE_NAME).connect()
        cursor = connectorObj.cursor()
        cursor.execute("SELECT * FROM taskInformation")
        rows = cursor.fetchall()
        self.tasks.clear()
        for row in rows:
            task = Task(row[0], row[1], row[2], row[3])
            self.tasks.append(task)
        cursor.close() 
        connectorObj.close()
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Tasks:")
            for task in self.tasks:
                print(f"ID: {task.task_id}, Name: {task.task_name}, Description: {task.task_description}, Status: {task.task_status}")
        # Clear the tasks list to avoid duplicates
        
            
    
    def mark_task_completed(self, task_id):
        connectorDet = dbConnect(DATABASE_NAME).connect()
        connectorCursor = connectorDet.cursor()
        sql = "UPDATE taskInformation SET task_status = 'Completed' WHERE task_id = %s"
        val = (task_id,)    
        connectorCursor.execute(sql, val)
        # Commit the changes to the database
        print(f"Task {task_id} marked as completed in database.")
        connectorDet.commit()
        connectorCursor.close() 
        connectorDet.close()
        # Update the task status in memory
        for task in self.tasks:
            if task.task_id == task_id:
                task.mark_completed()
                print(f"Task {task_id} marked as completed.")
                return True
        
        return False
    
    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        connectorDet = dbConnect(DATABASE_NAME).connect()
        connectorCursor = connectorDet.cursor()
        sql = "DELETE FROM taskInformation WHERE task_id = %s"
        val = (task_id,)
        connectorCursor.execute(sql, val)
        connectorCursor.close()
        connectorDet.commit()
        connectorDet.close()
        self.next_task_id -= 1
        # Delete the task from the database
        print(f"Task {task_id} deleted.")
    
    def getLatestTaskId(self):
        connectorObj = dbConnect(DATABASE_NAME).connect()
        cursor = connectorObj.cursor()
        cursor.execute("SELECT max(task_id) FROM taskInformation")
        rows = cursor.fetchall()
        next_task_id = 0
        if rows[0][0] is not None:
            next_task_id = rows[0][0] + 1
        else:
            next_task_id = 1
        cursor.close() 
        connectorObj.close()
        return next_task_id