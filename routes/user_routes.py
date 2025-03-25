from flask import request, jsonify, render_template, redirect, url_for, Blueprint
from datamanager.sqlite_data_manager import SQLiteDataManager
data_manager = SQLiteDataManager()
from datamanager.models import User

user = Blueprint('user', __name__)


@user.route('/users')
def list_users():
    users = data_manager.get_all_users()
    return render_template('users.html', users=users)

@user.route('/delete_user/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    data_manager.delete_user(user_id)
    return redirect(url_for('user.list_users'))



@user.route('/users/<int:user_id>')
def user_movies(user_id):
    movies = data_manager.get_user_movies(user_id)
    user_info = data_manager.get_user_from_id(user_id)
    return render_template('user_movies.html', movies=movies, user=user_info)

@user.route('/add_user', methods=['GET', 'POST'])
def add_user():
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