from abc import ABC, abstractmethod

class DataManagerInterface(ABC):
    """
    Abstract base class for data management. Enforces implementation of required methods in derived classes.
    """

    @abstractmethod
    def get_all_users(self):
        """
        Retrieve all users from the database.
        """
        pass

    @abstractmethod
    def get_user_movies(self, user_id):
        """
        Retrieve all movies associated with a specific user.

        Args:
            user_id (int): The unique identifier of the user.
        """
        pass

    @abstractmethod
    def get_user_from_id(self, user_id):
        """
        Retrieve a user's information based on their unique ID.

        Args:
            user_id (int): The unique identifier of the user.
        """
        pass

    @abstractmethod
    def add_user(self, user_data):
        """
        Add a new user to the database.

        Args:
            user_data (dict): A dictionary containing user details (e.g., first_name, last_name, etc.).
        """
        pass

    @abstractmethod
    def delete_user(self, user_id):
        """
        Delete a user based on their unique ID.

        Args:
            user_id (int): The unique identifier of the user to be deleted.
        """
        pass

    @abstractmethod
    def add_movie(self, user_id, title, director, year, rating):
        """
        Add a new movie to the database and associate it with a user.

        Args:
            user_id (int): The unique identifier of the user.
            title (str): The title of the movie.
            director (str): The director of the movie.
            year (str): The release year of the movie.
            rating (str): The rating of the movie.
        """
        pass

    @abstractmethod
    def add_user_movie(self, user_id, movie_id):
        """
        Associate a movie with a user.

        Args:
            user_id (int): The unique identifier of the user.
            movie_id (int): The unique identifier of the movie.
        """
        pass

    @abstractmethod
    def get_movie_from_id(self, movie_id):
        """
        Retrieve a movie's details based on its unique ID.

        Args:
            movie_id (int): The unique identifier of the movie.
        """
        pass

    @abstractmethod
    def update_movie(self, movie_id, movie_data):
        """
        Update an existing movie's details.

        Args:
            movie_id (int): The unique identifier of the movie.
            movie_data (dict): A dictionary containing updated movie details.
        """
        pass

    @abstractmethod
    def delete_movie(self, user_id, movie_id):
        """
        Delete a movie and disassociate it from a user.

        Args:
            user_id (int): The unique identifier of the user.
            movie_id (int): The unique identifier of the movie.
        """
        pass
