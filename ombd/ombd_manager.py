import json
import os
from dotenv import load_dotenv
import requests



load_dotenv()


class OMDIInterface:
    def __init__(self, movie_name):
        self.data = None
        self.movie_name = movie_name

    def __enter__(self):
        self.data = self.get_data()
        return self



    def get_data(self):
        base_url = "http://www.omdbapi.com/?t="
        path = self.movie_name
        api_tag = "&apikey="
        api_key = os.getenv("API_KEY")
        url = base_url + path + api_tag + api_key
        try:
            response = requests.get(url)
            if response.status_code != 200:
                logger.error(f"Error getting data from OMDI: {response.text}")
                return None
        except Exception as e:

            return None

        return json.loads(response.text)

    def parse_director(self):
        return self.data.get("Director")

    def parse_release_date(self):
        # Fix the int conversion to extract the year correctly
        date = int(self.data.get("Released")[-4:])
        return date

    def parse_rating(self):
        rating = float(self.data.get("Ratings")[0].get("Value").split("/")[0])
        return rating

    def parse_data(self):
        if self.data is None:
            print("nothing to see here")
            return False
        director = self.parse_director()
        release_date = self.parse_release_date()
        rating = self.parse_rating()


        return director, release_date, rating