from flask import request, jsonify, render_template, redirect, url_for, Blueprint
from datamanager.sqlite_data_manager import SQLiteDataManager
data_manager = SQLiteDataManager()

# Create a Blueprint for movie-related routes
movie = Blueprint('movie', __name__)

@movie.route('/users/<int:user_id>/add_movie', methods=['GET', 'POST'])
def add_movie(user_id):
    """
    Add a new movie to a user's list of favorites.

    Handles both GET and POST methods:
    - GET: Displays the 'add_movie.html' form for adding a new movie.
    - POST: Processes the submitted form data to add a new movie to the database
      and associates it with the given user.

    Form Data (POST):
        - title (str): The title of the movie.
        - year (str): The release year of the movie.
        - director (str): The movie's director.
        - rating (str): The rating of the movie.

    Args:
        user_id (int): The unique identifier of the user adding the movie.

    Returns:
        - On GET: Rendered HTML form to add a new movie.
        - On POST: Redirect response to the user's movie list page after adding the movie.
    """
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
    """
    Update details of a specific movie.

    Handles both GET and POST methods:
    - GET: Displays the 'update_movie.html' form pre-filled with existing movie data.
    - POST: Processes the submitted form data to update the movie's details in the database.

    Form Data (POST):
        - title (str): The title of the movie.
        - genre (str): The genre of the movie.
        - director (str): The movie's director.
        - year (str): The release year of the movie.
        - rating (str): The movie's rating.

    Args:
        user_id (int): The unique identifier of the user owning the movie.
        movie_id (int): The unique identifier of the movie being updated.

    Returns:
        - On GET: Rendered HTML form pre-filled with movie details.
        - On POST: Redirect response to the user's movie list page after updating the movie.
    """
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
    """
    Delete a specific movie from a user's list.

    This route deletes the movie identified by `movie_id` from the database
    and disassociates it from the given user.

    Args:
        user_id (int): The unique identifier of the user owning the movie.
        movie_id (int): The unique identifier of the movie being deleted.

    Returns:
        Redirect response to the user's movie list page after deletion.
    """
    data_manager.delete_movie(user_id, movie_id)
    return redirect(url_for('user.user_movies', user_id=user_id))
