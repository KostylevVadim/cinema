import psycopg2
from psycopg2 import Error


from data_fillers.from_csv import get_fromcsv
from data_fillers.films import film_series
from data_fillers.langs import lang
from data_fillers.users import users
from data_fillers.film_lang import film_lang
from data_fillers.person import person
from data_fillers.profs import profs 
from data_fillers.prec_sec import prese
from data_fillers.review import review 
from data_fillers.genre import genre, genre_film
from data_fillers.studio import studio
from data_fillers.sub import sub
from data_fillers.comp import comp
from data_fillers.film_connection import film_connection



connection = psycopg2.connect(user="postgres",
                                  password="123",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="cinema")

cursor = connection.cursor()


    
    





cursor.close()
connection.commit()
print("Соединение с PostgreSQL закрыто")


