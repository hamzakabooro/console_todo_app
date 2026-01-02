# Todo Application

A simple todo application with both console and web interfaces.

## Features

- Add, view, update, mark complete, and delete todo items
- Clean architecture with separation of concerns
- In-memory storage
- Both command-line and web interfaces

## Project Structure

```
src/
├── todo_app/
│   ├── models/
│   │   └── todo.py          # Todo data model
│   ├── services/
│   │   ├── store.py         # In-memory storage
│   │   └── todo_service.py  # Business logic
│   ├── cli/
│   │   ├── app.py           # CLI application
│   │   └── menu.py          # CLI menu
│   └── utils/
│       └── validators.py    # Input validation
├── main.py                  # Console application entry point
└── web_app.py               # Web application entry point
```

## Console Application

### Running the Console App

```bash
python main.py
```

### Console Features
- Interactive menu-driven interface
- Add, view, update, mark complete, and delete todos
- Input validation and error handling

## Web Application

### Running the Web App

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the web application:
```bash
python web_app.py
```

3. Open your browser and go to `http://localhost:5000`

### Web Features
- Clean, responsive user interface
- Add, edit, mark complete, and delete todos
- Real-time updates

## API Endpoints

The web application also provides a REST API:

- `GET /api/todos` - Get all todos
- `POST /api/todos` - Add a new todo
- `PUT /api/todos/<id>` - Update a todo
- `DELETE /api/todos/<id>` - Delete a todo
- `POST /api/todos/<id>/complete` - Mark a todo as complete

## Deployment

This application can be deployed to Vercel using the `vercel.json` configuration file.

## Architecture

The application follows a clean architecture pattern:

- **Models**: Define the data structures
- **Services**: Contain business logic
- **CLI/Web**: Handle user interaction
- **Utils**: Provide utility functions