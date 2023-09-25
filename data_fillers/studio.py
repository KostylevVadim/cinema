from random import randint
from datetime import date, timedelta
from random import choices

def studio(cursor):
    cursor.execute("SELECT id FROM film_series")
    record = cursor.fetchall()
    studios = ['Paramaunt','Walt Disney', 'Essanay','Mosfilm',
                'Warner Bros', '20th Century Fox','Sony','Columbia',
                'Universal','Miramax','Melnitsa','CTB','Sreda']
    for i in range(len(record)):
        cursor.execute("INSERT INTO studio (studioname, film_id) VALUES (%s , %s)",(studios[randint(0,12)],record[i]))

