# Data Model: Todo In-Memory Python Console Application

## Todo Entity

### Fields
- **id** (integer): Unique identifier for each todo item, automatically assigned
- **title** (string): Description text of the todo item, required
- **completed** (boolean): Status indicating whether the todo is completed (default: False)

### Validation Rules
- **id**: Must be unique within the application session, auto-generated
- **title**: Must not be empty or None, maximum length 500 characters
- **completed**: Must be a boolean value (True/False)

### State Transitions
- **Pending to Completed**: When user marks todo as completed using mark_complete() method
- **Completed to Pending**: Not supported (completed todos remain completed)

## In-Memory Store

### Structure
- **todos** (dictionary): Key-value store where key is the todo ID and value is the Todo object
- **next_id** (integer): Counter for generating unique IDs, starts at 1

### Operations
- **add(todo)**: Adds a new todo to the store with auto-generated ID
- **get(todo_id)**: Retrieves a todo by its ID
- **update(todo_id, updated_todo)**: Updates an existing todo
- **delete(todo_id)**: Removes a todo from the store
- **get_all()**: Returns all todos in the store
- **clear()**: Removes all todos from the store (not implemented in this application)

## Relationships
- No relationships exist between Todo entities in this simple application
- All todos are independent of each other