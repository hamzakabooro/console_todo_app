"""
Todo service layer that implements business logic for todo operations.
"""
from typing import List
from ..models.todo import Todo
from .store import InMemoryStore
from ..utils.validators import validate_todo_title, validate_todo_id


class TodoService:
    """
    Service layer that implements business logic for todo operations.
    """

    def __init__(self):
        """Initialize the service with an in-memory store."""
        self.store = InMemoryStore()

    def add_todo(self, title: str) -> int:
        """
        Add a new todo item to the store.

        Args:
            title: Description of the todo item

        Returns:
            ID of the created todo

        Raises:
            ValueError: If title is invalid
        """
        if not validate_todo_title(title):
            raise ValueError("Title must not be empty and must not exceed 500 characters")

        from ..models.todo import Todo
        # Create a new todo with a temporary ID (it will be overridden by the store)
        # We'll temporarily disable validation during creation
        todo = Todo.__new__(Todo)  # Create without calling __init__
        todo.id = 1  # Temporary ID, will be replaced by store
        todo.title = title
        todo.completed = False

        # Validate the fields manually without checking ID constraint
        if not isinstance(todo.title, str) or not todo.title:
            raise ValueError("Title must be a non-empty string")
        if not isinstance(todo.completed, bool):
            raise ValueError("Completed must be a boolean value")

        self.store.add(todo)
        return todo.id

    def get_todo(self, todo_id: int) -> Todo:
        """
        Retrieve a specific todo item by its ID.

        Args:
            todo_id: Unique identifier of the todo

        Returns:
            Todo object with id, title, and completed status

        Raises:
            KeyError: If todo with given ID doesn't exist
        """
        if not validate_todo_id(todo_id):
            raise KeyError(f"Invalid ID: {todo_id}")

        return self.store.get(todo_id)

    def get_all_todos(self) -> List[Todo]:
        """
        Retrieve all todo items in the store.

        Returns:
            List of all Todo objects
        """
        return self.store.get_all()

    def update_todo(self, todo_id: int, title: str) -> bool:
        """
        Update the title of an existing todo item.

        Args:
            todo_id: Unique identifier of the todo to update
            title: New description for the todo

        Returns:
            Boolean indicating success (True) or failure (False)

        Raises:
            KeyError: If todo with given ID doesn't exist
            ValueError: If title is invalid
        """
        if not validate_todo_id(todo_id):
            raise KeyError(f"Invalid ID: {todo_id}")

        if not validate_todo_title(title):
            raise ValueError("Title must not be empty and must not exceed 500 characters")

        # Get the current todo to preserve the completed status
        current_todo = self.store.get(todo_id)
        todo = Todo.__new__(Todo)  # Create without calling __init__
        todo.id = todo_id
        todo.title = title
        todo.completed = current_todo.completed  # Preserve the current completion status

        # Validate the fields manually without checking ID constraint
        if not isinstance(todo.title, str) or not todo.title:
            raise ValueError("Title must be a non-empty string")
        if not isinstance(todo.completed, bool):
            raise ValueError("Completed must be a boolean value")

        return self.store.update(todo_id, todo)

    def mark_complete(self, todo_id: int) -> bool:
        """
        Mark a specific todo item as completed.

        Args:
            todo_id: Unique identifier of the todo to mark complete

        Returns:
            Boolean indicating success (True) or failure (False)

        Raises:
            KeyError: If todo with given ID doesn't exist
        """
        if not validate_todo_id(todo_id):
            raise KeyError(f"Invalid ID: {todo_id}")

        # Get the current todo
        current_todo = self.store.get(todo_id)
        # Create an updated todo with completed status
        updated_todo = Todo.__new__(Todo)  # Create without calling __init__
        updated_todo.id = todo_id
        updated_todo.title = current_todo.title
        updated_todo.completed = True

        # Validate the fields manually without checking ID constraint
        if not isinstance(updated_todo.title, str) or not updated_todo.title:
            raise ValueError("Title must be a non-empty string")
        if not isinstance(updated_todo.completed, bool):
            raise ValueError("Completed must be a boolean value")

        # Update the store with the completed status
        return self.store.update(todo_id, updated_todo)

    def delete_todo(self, todo_id: int) -> bool:
        """
        Remove a specific todo item from the store.

        Args:
            todo_id: Unique identifier of the todo to delete

        Returns:
            Boolean indicating success (True) or failure (False)

        Raises:
            KeyError: If todo with given ID doesn't exist
        """
        if not validate_todo_id(todo_id):
            raise KeyError(f"Invalid ID: {todo_id}")

        return self.store.delete(todo_id)