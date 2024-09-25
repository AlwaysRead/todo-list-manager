import mysql.connector
from mysql.connector import Error
from tabulate import tabulate
from datetime import datetime

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="your_username",  
            password="your_password",  
            database="todo_list"
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def execute_query(connection, query, data=None):
    cursor = connection.cursor()
    try:
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def fetch_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

connection = create_connection()

create_tasks_table = """
CREATE TABLE IF NOT EXISTS tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    due_date DATE,
    status ENUM('pending', 'completed') DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""
execute_query(connection, create_tasks_table)

def add_task(connection):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    
    # Validate date input
    while True:
        due_date = input("Enter due date (YYYY-MM-DD): ")
        try:
            datetime.strptime(due_date, '%Y-%m-%d')
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
    
    # Validate status input
    while True:
        status = input("Enter status (pending/completed): ").lower()
        if status in ['pending', 'completed']:
            break
        else:
            print("Invalid status. Please enter 'pending' or 'completed'.")
    
    query = "INSERT INTO tasks (title, description, due_date, status) VALUES (%s, %s, %s, %s)"
    data = (title, description, due_date, status)
    execute_query(connection, query, data)

def update_task_status(connection):
    task_id = input("Enter task ID to update: ")
    
    # Validate status input
    while True:
        new_status = input("Enter new status (pending/completed): ").lower()
        if new_status in ['pending', 'completed']:
            break
        else:
            print("Invalid status. Please enter 'pending' or 'completed'.")
    
    query = "UPDATE tasks SET status = %s WHERE id = %s"
    data = (new_status, task_id)
    execute_query(connection, query, data)

def delete_task(connection):
    task_id = input("Enter task ID to delete: ")
    query = "DELETE FROM tasks WHERE id = %s"
    data = (task_id,)
    execute_query(connection, query, data)

def fetch_tasks(connection):
    query = "SELECT * FROM tasks"
    tasks = fetch_query(connection, query)
    headers = ["ID", "Title", "Description", "Due Date", "Status", "Created At"]
    print(tabulate(tasks, headers, tablefmt="pretty"))

def main():
    while True:
        print("\nTo-Do List Menu")
        print("1. Add Task")
        print("2. Update Task Status")
        print("3. Delete Task")
        print("4. View Tasks")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(connection)
        elif choice == "2":
            update_task_status(connection)
        elif choice == "3":
            delete_task(connection)
        elif choice == "4":
            fetch_tasks(connection)
        elif choice == "5":
            print("Exiting...")
            if connection.is_connected():
                connection.close()
                print("MySQL connection is closed")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
