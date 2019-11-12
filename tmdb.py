from dotenv import load_dotenv
import os
import locale
import requests
from datetime import datetime
import json

class TMDB:


    def __init__(self, id):
        self.id = id

        load_dotenv()
        API_KEY = os.getenv('TMDB_api_key')
        start_date = '2019-10-30'
        end_date = '2019-11-06'

        data = requests.get(f"https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&language=fr-FR&include_adult=false&include_video=false&page=1&primary_release_date.gte={start_date}&primary_release_date.lte={end_date}").json()

        self.title = data['Title']

        released = data['Released'].strip()
        release_date = datetime.strptime(released, '%d %b %Y')
        release_date_string = release_date.strftime('%Y-%m-%d')
        self.release_date = release_date_string

        self.original_title = data['original_title']

        self.tmId = data['id']