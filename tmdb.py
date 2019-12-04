from dotenv import load_dotenv
import os
import locale
import requests
import datetime
import json
from datetime import date

end_date = date.today()
delais = datetime.timedelta(days=7)

start_date = end_date - delais


# class TMDB:


    # def __init__(self):

load_dotenv()
API_KEY = os.getenv('TMDB_api_key')


datas = requests.get(f"https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&language=fr-FR&include_adult=false&include_video=false&page={page}&primary_release_date.gte={start_date}&primary_release_date.lte={end_date}").json()

numberpage = (datas['total_pages'])
print(numberpage)

# for page in range (0, numberpage):
#     movie[page]=requests.get(f"https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&language=fr-FR&include_adult=false&include_video=false&page={page}&primary_release_date.gte={start_date}&primary_release_date.lte={end_date}").json()
#     print(page)
#     # for movie in range(19):
#     #     print(datas[page]['results'][movie]['original_title'])





# for i in range (0,10):
#     result= (data['results'][i]['original_title'])
#     i += 1
# print(result)



        # self.title = data['Title']

        # released = data['Released'].strip()
        # release_date = datetime.strptime(released, '%d %b %Y')
        # release_date_string = release_date.strftime('%Y-%m-%d')
        # self.release_date = release_date_string

        # self.original_title = data['original_title']

        # self.tmId = data['id']