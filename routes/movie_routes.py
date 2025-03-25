from flask import request, jsonify, render_template, redirect, url_for, Blueprint
from datamanager.sqlite_data_manager import SQLiteDataManager
data_manager = SQLiteDataManager()

movie = Blueprint('movie', __name__)

@movie.route('/users/<int:user_id>/add_movie', methods=['GET', 'POST'])
def add_movie(user_id):
    if request.method == 'POST':
        title = request.form['title']

        year = request.form['year']
        director = request.form['director']
        rating = request.form['rating']
        new_id = data_manager.add_movie(user_id, title, director, year, rating)
        data_manager.add_user_movie(user_id, new_id)

        return redirect(url_for('user.user_movies', user_id=user_id))

    return render_template('add_movie.html', user_id=user_id)

@movie.route('/users/<int:user_id>/update_movie/<int:movie_id>', methods=['GET', 'POST'])
def update_movie(user_id, movie_id):
    movie = data_manager.get_movie_from_id(movie_id)
    print(movie_id)
    if request.method == 'POST':

        movie_data = {
            "movie_name": request.form['title'],
            "movie_genre": request.form['genre'],
            "movie_director": request.form['director'],
            "movie_release_date": request.form['year'],
            "movie_rating": request.form['rating']
        }

        data_manager.update_movie(movie_id, movie_data)
        return redirect(url_for('user.user_movies', user_id=user_id))
    return render_template('update_movie.html',
                           movie=movie,
                           user_id=user_id,
                           movie_id=movie_id)

@movie.route('/users/<int:user_id>/delete_movie/<int:movie_id>')
def delete_movie(user_id, movie_id):
    data_manager.delete_movie(user_id, movie_id)
    return redirect(url_for('user.user_movies', user_id=user_id))