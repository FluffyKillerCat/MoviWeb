# Description: all services related to the sql lite operations
from typing import override, Optional
from flask_sqlalchemy import SQLAlchemy
from datamanager.db import db
from datamanager.models import User, Movie, UserMovie
from datamanager.data_manager_interface import DataManagerInterface

UserDict = dict[str, str]
MovieDict = dict[str, str]


class SQLiteDataManager(DataManagerInterface):
    def __init__(self):
        self.db = db
        self.session = self.db.session
    def __exit__(self, exc_type, exc_value, traceback):
        """Clean up resources when the context is exited."""
        if self.session:
            self.session.remove()

    def __str__(self):
        return "SQLite Data Manager"

    def __repr__(self):
        return "SQLite Data Manager"

    @override
    def get_all_users(self) -> Optional[list[User]]:
        try:
            users = db.session.query(User).all()
            return users
        except Exception as e:
            return None


    def add_user(self, new_user: UserDict) -> None:
        try:
            self.session.add(
                User(
                    username=new_user["username"],
                    email=new_user["email"],
                    first_name=new_user["first_name"],
                    last_name=new_user["last_name"]
                )
            )
            self.session.commit()
            print(new_user)
        except Exception as e:
            self.session.rollback()


    def delete_user(self, user_id) -> None:
        """delete user from database"""
        try:
            user = self.get_user_from_id(user_id)
            self.session.delete(user)
            self.session.commit()
        except Exception as e:
            self.session.rollback()


    def update_user(self, user_id: int, new_user: UserDict) -> None:
        """modify user in database"""
        try:
            user = self.get_user_from_id(user_id)
            user.username = new_user["username"]
            user.email = new_user["email"]
            user.first_name = new_user["first_name"]
            user.last_name = new_user["last_name"]
            self.session.commit()
        except Exception as e:
            self.session.rollback()


    def get_all_movies(self) -> Optional[list[Movie]]:
        """get all movies from database"""
        try:
            return self.session.query(Movie).all()
        except Exception as e:
            return None


    def add_movie(self,user_id, title, director, year, rating):
        """add movie to db"""
        try:
            # Get movie data from OMDI API




            # Add movie to the database


            new_movie = Movie(
                movie_name=title,
                movie_director=director,
                movie_release_date=year,
                movie_rating=rating,
            )

            self.session.add(new_movie)
            self.session.commit()
            return new_movie.movie_id

        except Exception as e:
            self.session.rollback()


    def update_movie(self, movie_id, updated_movie):
        movie = self.get_movie_from_id(movie_id)
        if movie:
            movie.movie_name = updated_movie["movie_name"]
            movie.movie_director = updated_movie["movie_director"]
            movie.movie_release_date = updated_movie["movie_release_date"]
            movie.movie_rating = updated_movie["movie_rating"]
            self.session.commit()


    def delete_movie(self, user_id, movie_id):
        """delete movie from database"""
        movie = self.session.query(UserMovie).filter(
            UserMovie.user_id == user_id,
            UserMovie.movie_id == movie_id
        ).first()

        if movie:
            self.session.delete(movie)
            self.session.commit()

    # private Helper methods

    def get_movie_from_id(self, movie_id):
        """get movie from database"""
        movie = (
            self.session.query(Movie)
            .filter(Movie.movie_id == movie_id)
            .first()
        )
        return movie

    def get_user_from_id(self, user_id):
        """get movie from database"""
        user = self.session.query(User).filter(User.user_id == user_id).first()
        return user

    def get_user_movies(self, user_id):
        """get user movies from database"""
        user = self.get_user_from_id(user_id)
        return user.movies

    def add_user_movie(self, user_id, movie_id):
        """add user movie to database"""
        new_user_movie = UserMovie(user_id=user_id, movie_id=movie_id)
        self.session.add(new_user_movie)
        self.session.commit()
