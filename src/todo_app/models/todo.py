"""
Todo model representing a single todo item.
"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class Todo:
    """
    Represents a single todo item with id, title, and completion status.

    Attributes:
        id (int): Unique identifier for the todo item
        title (str): Description of the todo item
        completed (bool): Status indicating if the todo is completed
    """
    id: int
    title: str
    completed: bool = False

    def __post_init__(self):
        """Validate the todo after initialization."""
        if not isinstance(self.id, int) or self.id <= 0:
            raise ValueError("ID must be a positive integer")
        if not self.title or not isinstance(self.title, str):
            raise ValueError("Title must be a non-empty string")
        if not isinstance(self.completed, bool):
            raise ValueError("Completed must be a boolean value")