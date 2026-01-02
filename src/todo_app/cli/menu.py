"""
Menu interface for the todo CLI application.
"""


class TodoMenu:
    """
    Menu interface that handles user interaction and calls the todo service.
    """

    def __init__(self, todo_service):
        """Initialize the menu with a todo service."""
        self.todo_service = todo_service

    def display_menu(self):
        """Display the main menu options."""
        print("\n" + "="*30)
        print("1. Add Todo")
        print("2. View Todos")
        print("3. Update Todo")
        print("4. Mark Complete")
        print("5. Delete Todo")
        print("6. Exit")
        print("="*30)

    def handle_choice(self, choice: str):
        """Handle the user's menu choice."""
        if choice == '1':
            self._add_todo()
        elif choice == '2':
            self._view_todos()
        elif choice == '3':
            self._update_todo()
        elif choice == '4':
            self._mark_complete()
        elif choice == '5':
            self._delete_todo()
        else:
            print("Invalid option. Please choose a number from 1 to 6.")

    def _add_todo(self):
        """Handle adding a new todo."""
        title = input("Enter todo description: ").strip()
        try:
            todo_id = self.todo_service.add_todo(title)
            print(f"Todo added with ID: {todo_id}")
        except ValueError as e:
            print(f"Error: {e}")

    def _view_todos(self):
        """Handle viewing all todos."""
        todos = self.todo_service.get_all_todos()
        if not todos:
            print("No todos found.")
        else:
            print("\nYour Todos:")
            for todo in todos:
                status = "✓" if todo.completed else "○"
                print(f"{status} [{todo.id}] {todo.title}")

    def _update_todo(self):
        """Handle updating a todo."""
        try:
            todo_id = int(input("Enter todo ID to update: ").strip())
        except ValueError:
            print("Error: Please enter a valid integer ID.")
            return

        title = input("Enter new description: ").strip()
        try:
            success = self.todo_service.update_todo(todo_id, title)
            if success:
                print("Todo updated successfully.")
            else:
                print(f"Error: Todo with ID {todo_id} does not exist.")
        except ValueError as e:
            print(f"Error: {e}")

    def _mark_complete(self):
        """Handle marking a todo as complete."""
        try:
            todo_id = int(input("Enter todo ID to mark complete: ").strip())
        except ValueError:
            print("Error: Please enter a valid integer ID.")
            return

        try:
            success = self.todo_service.mark_complete(todo_id)
            if success:
                print("Todo marked as complete.")
            else:
                print(f"Error: Todo with ID {todo_id} does not exist.")
        except KeyError:
            print(f"Error: Todo with ID {todo_id} does not exist.")

    def _delete_todo(self):
        """Handle deleting a todo."""
        try:
            todo_id = int(input("Enter todo ID to delete: ").strip())
        except ValueError:
            print("Error: Please enter a valid integer ID.")
            return

        success = self.todo_service.delete_todo(todo_id)
        if success:
            print("Todo deleted successfully.")
        else:
            print(f"Error: Todo with ID {todo_id} does not exist.")