# Todo Service API Contract

## Todo Service Interface

### Methods

#### `add_todo(title: str) -> int`
- **Purpose**: Add a new todo item to the store
- **Input**: title (string) - description of the todo item
- **Output**: id (integer) - unique identifier of the created todo
- **Validation**:
  - Title must not be empty
  - Title must not exceed 500 characters
- **Error cases**:
  - ValueError if title is empty

#### `get_todo(todo_id: int) -> Todo`
- **Purpose**: Retrieve a specific todo item by its ID
- **Input**: todo_id (integer) - unique identifier of the todo
- **Output**: Todo object with id, title, and completed status
- **Error cases**:
  - KeyError if todo with given ID doesn't exist

#### `get_all_todos() -> List[Todo]`
- **Purpose**: Retrieve all todo items in the store
- **Input**: None
- **Output**: List of all Todo objects
- **Error cases**: None

#### `update_todo(todo_id: int, title: str) -> bool`
- **Purpose**: Update the title of an existing todo item
- **Input**: todo_id (integer), title (string)
- **Output**: boolean indicating success (True) or failure (False)
- **Validation**:
  - Title must not be empty
  - Title must not exceed 500 characters
- **Error cases**:
  - KeyError if todo with given ID doesn't exist
  - ValueError if title is empty

#### `mark_complete(todo_id: int) -> bool`
- **Purpose**: Mark a specific todo item as completed
- **Input**: todo_id (integer)
- **Output**: boolean indicating success (True) or failure (False)
- **Error cases**:
  - KeyError if todo with given ID doesn't exist

#### `delete_todo(todo_id: int) -> bool`
- **Purpose**: Remove a specific todo item from the store
- **Input**: todo_id (integer)
- **Output**: boolean indicating success (True) or failure (False)
- **Error cases**:
  - KeyError if todo with given ID doesn't exist

## Todo Model Contract

### Properties
- `id: int` - Unique identifier (read-only after creation)
- `title: str` - Description text
- `completed: bool` - Completion status (default: False)

### Validation
- `id` must be a positive integer
- `title` must not be empty or None
- `completed` must be a boolean value