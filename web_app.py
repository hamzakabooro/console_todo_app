from flask import Flask, render_template, request, jsonify, redirect, url_for
from src.todo_app.services.todo_service import TodoService

app = Flask(__name__)
# Use a global instance of the service (in production, you'd want a better state management)
todo_service = TodoService()


@app.route('/')
def index():
    """Main page showing all todos."""
    todos = todo_service.get_all_todos()
    return render_template('index.html', todos=todos)


@app.route('/add', methods=['POST'])
def add_todo():
    """Add a new todo."""
    title = request.form.get('title', '').strip()
    if title:
        todo_id = todo_service.add_todo(title)
    return redirect(url_for('index'))


@app.route('/update/<int:todo_id>', methods=['POST'])
def update_todo(todo_id):
    """Update a todo."""
    title = request.form.get('title', '').strip()
    if title:
        todo_service.update_todo(todo_id, title)
    return redirect(url_for('index'))


@app.route('/complete/<int:todo_id>', methods=['POST'])
def mark_complete(todo_id):
    """Mark a todo as complete."""
    todo_service.mark_complete(todo_id)
    return redirect(url_for('index'))


@app.route('/delete/<int:todo_id>', methods=['POST'])
def delete_todo(todo_id):
    """Delete a todo."""
    todo_service.delete_todo(todo_id)
    return redirect(url_for('index'))


@app.route('/api/todos', methods=['GET'])
def api_get_todos():
    """API endpoint to get all todos."""
    todos = todo_service.get_all_todos()
    return jsonify([{
        'id': todo.id,
        'title': todo.title,
        'completed': todo.completed
    } for todo in todos])


@app.route('/api/todos', methods=['POST'])
def api_add_todo():
    """API endpoint to add a todo."""
    data = request.get_json()
    title = data.get('title', '').strip()
    if title:
        todo_id = todo_service.add_todo(title)
        return jsonify({'id': todo_id}), 201
    return jsonify({'error': 'Title is required'}), 400


@app.route('/api/todos/<int:todo_id>', methods=['PUT'])
def api_update_todo(todo_id):
    """API endpoint to update a todo."""
    data = request.get_json()
    title = data.get('title', '').strip()
    if title:
        success = todo_service.update_todo(todo_id, title)
        if success:
            return jsonify({'success': True})
    return jsonify({'error': 'Failed to update todo'}), 400


@app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def api_delete_todo(todo_id):
    """API endpoint to delete a todo."""
    success = todo_service.delete_todo(todo_id)
    if success:
        return jsonify({'success': True})
    return jsonify({'error': 'Failed to delete todo'}), 400


@app.route('/api/todos/<int:todo_id>/complete', methods=['POST'])
def api_mark_complete(todo_id):
    """API endpoint to mark a todo as complete."""
    success = todo_service.mark_complete(todo_id)
    if success:
        return jsonify({'success': True})
    return jsonify({'error': 'Failed to mark complete'}), 400


if __name__ == '__main__':
    app.run(debug=True)