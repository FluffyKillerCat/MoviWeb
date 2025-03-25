from flask import request, jsonify, render_template, redirect, url_for, Blueprint
from datamanager.sqlite_data_manager import SQLiteDataManager
data_manager = SQLiteDataManager()
from datamanager.models import User

# Create a Blueprint for user-related routes
user = Blueprint('user', __name__)

@user.route('/users')
def list_users():
    """
    Fetch and display a list of all users.

    This route retrieves all user data from the database
    using the data manager and renders it in the 'users.html' template.

    Returns:
        Rendered HTML template displaying the list of users.
    """
    users = data_manager.get_all_users()
    return render_template('users.html', users=users)

@user.route('/delete_user/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    """
    Delete a specific user by their ID.

    This route deletes the user identified by `user_id` from the database
    using the data manager and redirects to the user list page.

    Args:
        user_id (int): The unique identifier of the user to delete.

    Returns:
        Redirect response to the user list page.
    """
    data_manager.delete_user(user_id)
    return redirect(url_for('user.list_users'))

@user.route('/users/<int:user_id>')
def user_movies(user_id):
    """
    Display a specific user's favorite movies.

    This route retrieves all movies associated with a specific user
    using their `user_id`, along with the user's information.
    The data is rendered in the 'user_movies.html' template.

    Args:
        user_id (int): The unique identifier of the user.

    Returns:
        Rendered HTML template displaying the user's movies and information.
    """
    movies = data_manager.get_user_movies(user_id)
    user_info = data_manager.get_user_from_id(user_id)
    return render_template('user_movies.html', movies=movies, user=user_info)

@user.route('/add_user', methods=['GET', 'POST'])
def add_user():
    """
    Add a new user to the system.

    Handles both GET and POST methods:
    - GET: Displays the 'add_user.html' form for adding a new user.
    - POST: Processes the submitted form data and adds a new user to the database.

    Form Data (POST):
        - first_name (str): The user's first name.
        - last_name (str): The user's last name.
        - username (str): The user's username.
        - email (str): The user's email address.

    Returns:
        - On GET: Rendered HTML form to add a new user.
        - On POST: Redirect response to the user list page after adding the user.
    """
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        username = request.form['username']
        email = request.form['email']

        _user = {
            'first_name': first_name,
            'last_name': last_name,
            'username': username,
            'email': email
        }

        data_manager.add_user(_user)
        return redirect(url_for('user.list_users'))

    return render_template('add_user.html')
@user.route('/update_user/<int:user_id>', methods=['GET', 'POST'])
def update_user(user_id):
    """
    Update a user's information in the database.

    Handles both GET and POST methods:
    - GET: Displays the 'update_user.html' form pre-filled with existing user data.
    - POST: Processes the submitted form data to update the user's information.

    Args:
        user_id (int): The unique identifier of the user to update.

    Returns:
        - On GET: Rendered HTML form pre-filled with user details.
        - On POST: Redirect response to the user list page after updating the user.
    """
    user_data = data_manager.get_user_from_id(user_id)

    if request.method == 'POST':
        # Collect form data
        new_user = {
            "username": request.form['username'],
            "email": request.form['email'],
            "first_name": request.form['first_name'],
            "last_name": request.form['last_name']
        }

        # Update user in database
        data_manager.update_user(user_id, new_user)

        return redirect(url_for('user.list_users'))

    return render_template('update_user.html', user=user_data, user_id=user_id)
