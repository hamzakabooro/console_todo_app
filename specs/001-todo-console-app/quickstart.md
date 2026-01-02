# Quickstart Guide: Todo In-Memory Python Console Application

## Prerequisites
- Python 3.13+ installed on your system
- Basic knowledge of command-line interfaces

## Setup
1. Clone or create the project directory structure as specified in the plan
2. Ensure you have Python 3.13+ installed: `python --version`
3. No additional dependencies required (using Python standard library only)

## Running the Application
1. Navigate to the project root directory
2. Execute: `python main.py`
3. The application will start and display the main menu

## Available Operations
1. **Add Todo**: Enter option 1 to add a new todo item with a description
2. **View Todos**: Enter option 2 to see all current todo items
3. **Update Todo**: Enter option 3 to modify an existing todo's description
4. **Mark Complete**: Enter option 4 to mark a todo as completed
5. **Delete Todo**: Enter option 5 to remove a todo from the list
6. **Exit**: Enter option 6 to quit the application

## Example Usage
```
Welcome to the Todo Application!
1. Add Todo
2. View Todos
3. Update Todo
4. Mark Complete
5. Delete Todo
6. Exit
Choose an option: 1
Enter todo description: Buy groceries
Todo added with ID: 1
```

## Testing
To run the unit tests:
1. Navigate to the project root directory
2. Execute: `pytest tests/`
3. All tests should pass if the implementation is correct

## Notes
- All data is stored in memory only and will be lost when the application exits
- The application validates user input and provides appropriate error messages
- Each todo has a unique identifier assigned automatically