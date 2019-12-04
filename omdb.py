import locale
import requests
from datetime import datetime
import os
from dotenv import load_dotenv

class OMDB:
    


    def __init__(self, id):
        self.id = id
        
        load_dotenv()
        API_KEY = os.getenv('OMDB_api_key')

        data = requests.get(f"http://www.omdbapi.com/?apikey={API_KEY}&i={id}").json()  # on va chercher l'id du film sur l'API, en incluant la key

        self.title = data['Title']

        self.duration = int(data['Runtime'].split('m')[0].strip())  # on change la valeur de l'api qui est en string, pour le mettre en INT. on split à partir de 'm' et on garde la prmiere partie =>[0]. Puis on 'Strip' pour enlever les espaces

        released = data['Released'].strip()   # idem que pour le runtime 
        release_date = datetime.strptime(released, '%d %b %Y') # on mets en forme la date
        release_date_string = release_date.strftime('%Y-%m-%d')
        self.release_date = release_date_string

        self.original_title = data['Title']

        self.rating = data['Rated']
        if self.rating == "PG":
            self.rating = "TP"
        if self.rating == "PG-13":
            self.rating = "-12"
        if self.rating == "R":
            self.rating = "-16"
        if self.rating == "NC-17":
            self.rating = "-18"
        
        self.imdbId = data['imdbID']
        

     #  self.revenue = 'NULL'
        locale.setlocale(locale.LC_ALL, 'en_US.UTF8')  # on met en forme le revenue, en passant de $47,787,845 à 47787845 par ex
        if data['BoxOffice'] != "N/A":
            self.revenue = int(locale.atof(data['BoxOffice'].strip("$")))
        else:
            self.revenue = None
        

        self.actors = []
        actor = data['Actors'].split(',')  # on cree une liste des Actors depuis "Actors" dans le Json, on separe les noms (entre chaque ,)
        for person in range(len(actor)):  # dans tout le range de la liste actor, on separe nom et prenom, grace au split avant et apres l'espace " "
            name_separated = actor[person].strip().split(' ')
            self.actors.append(name_separated)