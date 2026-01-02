"""
Input validation utilities for the todo application.
"""


def validate_todo_title(title: str) -> bool:
    """
    Validate a todo title according to the specification.

    Args:
        title: The title to validate

    Returns:
        True if the title is valid, False otherwise
    """
    if not title:
        return False
    if not isinstance(title, str):
        return False
    if len(title) > 500:
        return False
    return True


def validate_todo_id(todo_id: int) -> bool:
    """
    Validate a todo ID according to the specification.

    Args:
        todo_id: The ID to validate

    Returns:
        True if the ID is valid, False otherwise
    """
    if not isinstance(todo_id, int):
        return False
    if todo_id <= 0:
        return False
    return True