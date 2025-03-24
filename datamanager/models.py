from sqlalchemy import Integer, String, Float

from datamanager.db import db


class User(db.Model):
    __tablename__ = "users"
    __table_args__ = {"extend_existing": True}
    user_id = db.Column(Integer, primary_key=True, autoincrement=True)
    username = db.Column(String(50), unique=True)
    email = db.Column(String(50), unique=True)
    first_name = db.Column(String(50))
    last_name = db.Column(String(50))
    movies = db.relationship(
        "Movie",
        secondary="user_movies",  # Name of the association table
        backref="users",
    )

    def __repr__(self):
        return (
            f"<User(id={self.user_id}',"
            f"username='{self.username}', "
            f"email='{self.email}', "
            f"first_name='{self.first_name}', "
            f"last_name='{self.last_name}')>"
        )

    def __str__(self):
        return f"{self.username}"


class Movie(db.Model):
    __tablename__ = "movies"
    __table_args__ = {"extend_existing": True}
    movie_id = db.Column(Integer, primary_key=True, autoincrement=True)
    movie_name = db.Column(String(50))
    movie_director = db.Column(String(50))
    movie_release_date = db.Column(Integer)
    movie_rating = db.Column(Float)

    def __repr__(self):
        return (
            f"<Movie(id='{self.movie_id}',"
            f"name='{self.movie_name}', "
            f"director='{self.movie_director}', "
            f"release_date='{self.movie_release_date}', "
            f"rating='{self.movie_rating}')>"
        )

    def __str__(self):
        return f"{self.movie_name}"


class UserMovie(db.Model):
    __tablename__ = "user_movies"
    __table_args__ = {"extend_existing": True}
    user_id = db.Column(
        Integer, db.ForeignKey("users.user_id"), primary_key=True
    )
    movie_id = db.Column(
        Integer, db.ForeignKey("movies.movie_id"), primary_key=True
    )


    def __repr__(self):
        return (
            f"<UserMovie(id={self.user_movie_id}',"
            f"user_id='{self.user_id}', "
            f"movie_id='{self.movie_id}')>"
        )

    def __str__(self):
        return f"{self.user_id} - {self.movie_id}"





