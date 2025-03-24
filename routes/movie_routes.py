from flask import request, jsonify, render_template, redirect, url_for, Blueprint
from datamanager.sqlite_data_manager import SQLiteDataManager
data_manager = SQLiteDataManager()

movie = Blueprint('movie', __name__)

@movie.route('/users/<int:user_id>/add_movie', methods=['GET', 'POST'])
def add_movie(user_id):
    if request.method == 'POST':
        title = request.form['title']
        genre = request.form['genre']
        data_manager.add_movie(user_id, title, genre)
        return redirect(url_for('user_movies', user_id=user_id))
    return render_template('add_movie.html', user_id=user_id)

@movie.route('/users/<int:user_id>/update_movie/<int:movie_id>', methods=['GET', 'POST'])
def update_movie(user_id, movie_id):
    movie = data_manager.get_movie(movie_id)
    if request.method == 'POST':
        title = request.form['title']
        genre = request.form['genre']
        data_manager.update_movie(movie_id, title, genre)
        return redirect(url_for('user_movies', user_id=user_id))
    return render_template('update_movie.html', movie=movie, user_id=user_id)

@movie.route('/users/<int:user_id>/delete_movie/<int:movie_id>', methods=['POST'])
def delete_movie(user_id, movie_id):
    data_manager.delete_movie(movie_id)
    return redirect(url_for('user_movies', user_id=user_id))