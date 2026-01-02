#!/usr/bin/env python3
"""
Main entry point for the Todo Application.
"""
from src.todo_app.cli.app import TodoApp


def main():
    """Main function to start the application."""
    app = TodoApp()
    app.run()


if __name__ == "__main__":
    main()