from flask import request, jsonify, render_template, redirect, url_for, Blueprint
from datamanager.sqlite_data_manager import SQLiteDataManager
data_manager = SQLiteDataManager()

user = Blueprint('user', __name__)


@user.route('/users')
def list_users():
    users = data_manager.get_all_users()
    return render_template('users.html', users=users)

@user.route('/users/<int:user_id>')
def user_movies(user_id):
    movies = data_manager.get_user_movies(user_id)
    return render_template('user_movies.html', movies=movies, user_id=user_id)

@user.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        username = request.form['username']
        data_manager.add_user(username)
        return redirect(url_for('list_users'))
    return render_template('add_user.html')