Task Manager (MySQL + Python)


This is a simple command-line task management application built using Python and MySQL. It allows users to add, update, delete, and view tasks, complete with due dates and status tracking.
Features
- Add Tasks: Users can create tasks with a title, description, due date, and status (pending/completed).
- Update Task Status: Change the status of tasks between 'pending' and 'completed'.
- Delete Tasks: Remove tasks by their unique ID.
- View All Tasks: Display all tasks in a table format with details such as title, description, due date, and status.
Technologies Used
- Python: Core programming language for backend logic.
- MySQL: Relational database used to store tasks.
- Tabulate: Python library to display tasks in a table format in the terminal.
Prerequisites
Before running the project, ensure you have the following installed:
- Python 3.x
- MySQL
- `mysql-connector-python` package
- `tabulate` package
Install MySQL Connector and Tabulate
Run the following command:
```bash
pip install mysql-connector-python tabulate
```
Getting Started
1. Clone the Repository
```bash
git clone https://github.com/yourusername/repository-name.git
cd repository-name
```
2. Set Up MySQL Database
Open MySQL and create a new database:
```sql
CREATE DATABASE todo_list;
```
Update the `create_connection()` function in the script to match your MySQL credentials:
```python
connection = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="todo_list"
)
```
3. Run the Application
Simply run the Python script and follow the on-screen menu:
```bash
python task_manager.py
```
Usage
Once you run the program, you will see the following menu:
```
To-Do List Menu:
1. Add Task
2. Update Task Status
3. Delete Task
4. View Tasks
5. Exit
```

Sample Output
```bash
+----+----------------+------------------------+------------+------------+---------------------+-------+
| ID  | Title          		| Description           	| Due Date   | Status    | Created At          |
+----+----------------+------------------------+------------+------------+---------------------+-------+
|  1  | Complete Project    | Finish the Python script  | 2023-09-30 | pending   | 2023-09-25 14:12:30 |
|  2  | Read Book           | Read 50 pages of a novel  | 2023-10-01 | completed | 2023-09-25 14:13:45 |
+----+----------------+------------------------+------------+------------+---------------------+-------+
```
Future Enhancements
- User authentication for managing individual task lists.
- Add categories or priority levels to tasks.
- Export tasks to a CSV or JSON file.
Contributing
Feel free to fork this project, submit pull requests, or open issues for any bug reports or feature suggestions.
All the works were done by me myself, feel free to add any reviews and improvements :)
