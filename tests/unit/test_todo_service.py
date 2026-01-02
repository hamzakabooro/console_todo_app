"""
Unit tests for the todo service.
"""
import pytest
from src.todo_app.services.todo_service import TodoService
from src.todo_app.models.todo import Todo


class TestTodoService:
    """Test cases for the TodoService class."""

    def setup_method(self):
        """Set up a fresh service instance for each test."""
        self.service = TodoService()

    def test_add_todo_success(self):
        """Test adding a todo successfully."""
        title = "Test todo"
        todo_id = self.service.add_todo(title)

        assert todo_id == 1
        todos = self.service.get_all_todos()
        assert len(todos) == 1
        assert todos[0].id == 1
        assert todos[0].title == title
        assert todos[0].completed is False

    def test_add_todo_empty_title_fails(self):
        """Test that adding a todo with empty title raises ValueError."""
        with pytest.raises(ValueError):
            self.service.add_todo("")

    def test_add_todo_long_title_fails(self):
        """Test that adding a todo with too long title raises ValueError."""
        long_title = "x" * 501  # More than 500 characters
        with pytest.raises(ValueError):
            self.service.add_todo(long_title)

    def test_get_todo_success(self):
        """Test getting a specific todo."""
        title = "Test todo"
        todo_id = self.service.add_todo(title)

        todo = self.service.get_todo(todo_id)
        assert todo.id == todo_id
        assert todo.title == title
        assert todo.completed is False

    def test_get_todo_invalid_id_fails(self):
        """Test that getting a non-existent todo raises KeyError."""
        with pytest.raises(KeyError):
            self.service.get_todo(999)

    def test_get_all_todos(self):
        """Test getting all todos."""
        titles = ["Todo 1", "Todo 2", "Todo 3"]
        for title in titles:
            self.service.add_todo(title)

        todos = self.service.get_all_todos()
        assert len(todos) == 3
        for i, todo in enumerate(todos):
            assert todo.id == i + 1
            assert todo.title == titles[i]
            assert todo.completed is False

    def test_update_todo_success(self):
        """Test updating a todo's title."""
        original_title = "Original todo"
        todo_id = self.service.add_todo(original_title)
        new_title = "Updated todo"

        success = self.service.update_todo(todo_id, new_title)
        assert success is True

        updated_todo = self.service.get_todo(todo_id)
        assert updated_todo.title == new_title

    def test_update_todo_preserves_completion_status(self):
        """Test that updating a todo preserves its completion status."""
        title = "Test todo"
        todo_id = self.service.add_todo(title)

        # Mark as complete
        self.service.mark_complete(todo_id)

        # Update the title
        new_title = "Updated todo"
        self.service.update_todo(todo_id, new_title)

        # Verify the completion status is preserved
        updated_todo = self.service.get_todo(todo_id)
        assert updated_todo.completed is True
        assert updated_todo.title == new_title

    def test_update_todo_invalid_id_fails(self):
        """Test that updating a non-existent todo returns False."""
        result = self.service.update_todo(999, "New title")
        assert result is False

    def test_mark_complete_success(self):
        """Test marking a todo as complete."""
        title = "Test todo"
        todo_id = self.service.add_todo(title)

        success = self.service.mark_complete(todo_id)
        assert success is True

        todo = self.service.get_todo(todo_id)
        assert todo.completed is True

    def test_mark_complete_invalid_id_fails(self):
        """Test that marking a non-existent todo raises KeyError."""
        with pytest.raises(KeyError):
            self.service.mark_complete(999)

    def test_delete_todo_success(self):
        """Test deleting a todo."""
        title = "Test todo"
        todo_id = self.service.add_todo(title)

        success = self.service.delete_todo(todo_id)
        assert success is True

        todos = self.service.get_all_todos()
        assert len(todos) == 0

    def test_delete_todo_invalid_id_fails(self):
        """Test that deleting a non-existent todo returns False."""
        result = self.service.delete_todo(999)
        assert result is False