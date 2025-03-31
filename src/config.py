# config.py

TASKS_FILE = "tasks.json"  # File to store tasks
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"  # Standard date format
MAX_TASKS = 100  # Maximum allowed tasks

# File-based storage
TASK_STORAGE_FILE = "data/tasks.json"

# Database storage (if using SQLite)
DATABASE_URI = "sqlite:///tasks.db"
DATABASE_NAME = "task"