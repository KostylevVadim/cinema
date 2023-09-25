from random import randint, choice
def profs(cursor):
    cursor.execute('SELECT * FROM film_series')
    films = cursor.fetchall()
    cursor.execute('SELECT * FROM person')
    persons = cursor.fetchall()
    workers = ['Director', 'Operator', 'Actor', 'Producer', 'Scriptwriter', 'Stuff']
    for person in persons:
        #print(person)
        birth = person[2]
        death = person[3]
        cursor.execute('SELECT * FROM film_series WHERE  date_real > %s and  date_real < %s', (birth, death))
        сould_work_here = cursor.fetchall()
        
        for film in сould_work_here:
            x = randint(0,2)
            if x==1:
                w = randint(0, len(workers)-1)
                work = workers[w]
                print(film[0], person[0], work)
                cursor.execute('INSERT INTO profession (film_id, prof, per_id) VALUES (%s, %s, %s)', (int(film[0]), str(work), int(person[0])))
        

