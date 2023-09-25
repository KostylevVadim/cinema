import psycopg2
from psycopg2 import Error
from random import randint
from datetime import date, timedelta
from random import choices
import time    
import random
import string
def film_series(cursor, count):
    film_firstnames = ['Walk','Brother','Star', 'The', 'Under', 'Driving', 'White','Leaving',
                        'Wild','Flash', 'Lord', 'Back', 'Some','Park',
                        'Thunder', 'Robot', 'Kingdom','Iron','Killer',
                        'Leter ', 'Runner'
                        ]
    film_lastnames = [' line',' dwarf',' predator',' of Las Vegas',' Heart',
                        ' dance', ' ring',' future', ' problems',
                        ' of zombie', ' in heart',' from space',
                        ' of heaven',' man', ' traffic', ' beach', ' effect',
                        ' valkyre',' sneakers', ' guy', ' death',' fortune',
                        ' signe', ' scorpion', ' wife', ' lands', ' road', 
                        ' scream', ' gun',' revolver', ' escape', ' catcher',
                        ' from sun', ' from Van Helsing', ' end', ' spy'] 
    for i in range(count):
        fullfilmname = film_firstnames[randint(0,len(film_firstnames)-1)] + film_lastnames[randint(0,len(film_lastnames)-1)]
        test_date1, test_date2 = date(1920, 6, 3), date(2020, 7, 1)
        born_delta = randint(0,35000)
        born_date = test_date1 + timedelta(days=born_delta)
        film_or_series = bool(randint(0,1))
        season = 0
        series = 0
        if(film_or_series == False):
            season = randint(1,245)
            series = randint(1,50)
        rating = 0.0
        age = [3,7,12,16,18]
        age_real = age[randint(0,len(age)-1)]
        cost = float(randint(10000,99999))/10
        
        if(film_or_series == True):
            
            cursor.execute("INSERT INTO film_series (film_name,date_real,age,filorser,cost) VALUES(%s,%s,%s,%s,%s)",
            (fullfilmname,born_date,age_real,film_or_series,cost))
            
            

        else:
            cursor.execute("INSERT INTO film_series (film_name,date_real,age,filorser,cost,season,series) VALUES(%s,%s,%s,%s,%s,%s,%s)",
            (fullfilmname,born_date,age_real,film_or_series,cost,season,series))
    