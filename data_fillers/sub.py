from random import randint
from datetime import date, timedelta
from random import choices

def sub(cursor):
    cursor.execute("SELECT (id) FROM film_series WHERE(filorser = True)")
    record = cursor.fetchall()
    future_sub = []

    for i in range(len(record)):
        if(randint(0,1)==0):
            future_sub.append(record[i][0])
            cursor.execute("INSERT INTO sub SELECT (id) FROM film_series WHERE film_series.id = %s",(record[i]))
