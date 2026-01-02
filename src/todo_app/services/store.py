"""
In-memory store for todo items.
"""
from typing import Dict, List
from ..models.todo import Todo


class InMemoryStore:
    """
    In-memory store for managing todo items.

    This store uses a dictionary to hold todos with their IDs as keys.
    It also maintains a counter for generating unique IDs.
    """

    def __init__(self):
        """Initialize the store with an empty dictionary and ID counter."""
        self._todos: Dict[int, Todo] = {}
        self._next_id: int = 1

    def add(self, todo: Todo) -> None:
        """
        Add a new todo to the store with auto-generated ID.

        Args:
            todo: The todo item to add (ID will be ignored, a new one will be assigned)
        """
        # Assign a new ID to the todo
        todo.id = self._next_id
        self._todos[self._next_id] = todo
        self._next_id += 1

    def get(self, todo_id: int) -> Todo:
        """
        Retrieve a todo by its ID.

        Args:
            todo_id: The ID of the todo to retrieve

        Returns:
            The todo item with the specified ID

        Raises:
            KeyError: If no todo with the given ID exists
        """
        if todo_id not in self._todos:
            raise KeyError(f"Todo with ID {todo_id} does not exist")
        return self._todos[todo_id]

    def update(self, todo_id: int, updated_todo: Todo) -> bool:
        """
        Update an existing todo.

        Args:
            todo_id: The ID of the todo to update
            updated_todo: The updated todo item

        Returns:
            True if the update was successful, False otherwise
        """
        if todo_id not in self._todos:
            return False

        # Preserve the original ID
        updated_todo.id = todo_id
        self._todos[todo_id] = updated_todo
        return True

    def delete(self, todo_id: int) -> bool:
        """
        Remove a todo from the store.

        Args:
            todo_id: The ID of the todo to remove

        Returns:
            True if the deletion was successful, False otherwise
        """
        if todo_id not in self._todos:
            return False

        del self._todos[todo_id]
        return True

    def get_all(self) -> List[Todo]:
        """
        Return all todos in the store.

        Returns:
            A list of all todo items
        """
        return list(self._todos.values())