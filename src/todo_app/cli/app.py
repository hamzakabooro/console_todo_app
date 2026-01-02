"""
Main application entry point for the todo CLI application.
"""
from .menu import TodoMenu
from ..services.todo_service import TodoService


class TodoApp:
    """
    Main application class that manages the CLI interface and service layer.
    """

    def __init__(self):
        """Initialize the application with a todo service and menu."""
        self.todo_service = TodoService()
        self.menu = TodoMenu(self.todo_service)

    def run(self):
        """Start the main application loop."""
        print("Welcome to the Todo Application!")
        while True:
            try:
                self.menu.display_menu()
                choice = input("Choose an option: ").strip()
                if choice == '6':
                    print("Goodbye!")
                    break
                self.menu.handle_choice(choice)
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except Exception as e:
                print(f"An error occurred: {e}")