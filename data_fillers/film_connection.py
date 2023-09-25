import random
def film_connection(cursor):
    cursor.execute('SELECT id, film_name From film_series Order By date_real')
    films = cursor.fetchall()
    for i in range(len(films)-1):
        film = films[i]
        film_name = film[1].split()
        film_id = film[0]
        # print(film_id, film_name)
        for j in range(i+1, len(films)):
            cursor.execute('SELECT seq_id FROM film_connection WHERE seq_id=%s',(films[j][0],))
            f = cursor.fetchall()
            film_name1 = films[j][1].split()
            cursor.execute('SELECT prec_id FROM film_connection WHERE prec_id=%s', (film_id,))
            f1 = cursor.fetchall()
            if len(f)==0 and film_name[0] == film_name1[0] and len(f1)==0:
                cursor.execute('INSERT INTO film_connection(prec_id, seq_id) VALUES(%s,%s)', (film_id,films[j][0]))

            

        