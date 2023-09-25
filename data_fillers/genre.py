from random import randint
def genre(cursor):
    ganre = ['action','adventure','animated',
            'comedy','drama','fantasy','historical',
            'horror','noir','science fiction','Thriller',
            'Western']

    for i in range(len(ganre)-1):
        cursor.execute("INSERT INTO genre (id, ganre) VALUES(%s,%s)",
            (i,ganre[i]))
        
def genre_film(cursor):
    cursor.execute("SELECT id FROM film_series")
    record1=cursor.fetchall()
    cursor.execute("SELECT id FROM genre")
    record2=cursor.fetchall()
    for i in range(len(record1)):
        x = randint(0,len(record2)-1)
        print(record1[i],' ',record2[x])
        cursor.execute("INSERT INTO filmganre (film_id, ganre_id) VALUES (%s,%s)",(record1[i],record2[x]))