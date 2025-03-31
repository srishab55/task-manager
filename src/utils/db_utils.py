import mysql.connector
class dbConnect:
    def __init__(self, db_name):
        self.db_name = db_name

    def connect(self):
        # Simulate a database connection
        print(f"Connecting to database: {self.db_name}")
        conn = mysql.connector.connect(
        host="localhost",
        database=self.db_name,
        user="root",
        password="password here", ### replace with your password
        port="3306"
        )
        return conn

    def disconnect(self):
        # Simulate closing the database connection
        print(f"Disconnecting from database: {self.db_name}")
        return True