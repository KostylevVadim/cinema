from random import randint
def film_lang(cursor):
    cursor.execute('SELECT * FROM film_series')
    record1 = cursor.fetchall()
    cursor.execute("SELECT id FROM lang")
    record2 = cursor.fetchall()
    for i in range(len(record1)):
        how_many_langs = randint(1,7)
        un = []
        for j in range(how_many_langs):
            x = randint(0,len(record2)-1)
            if record2[x][0] in un:
                continue
            else:
                un.append(record2[x][0])
        
        for m in range(len(un)):
            cursor.execute("INSERT INTO film_lang (film_id, lang_id) VALUES (%s,%s)",(record1[i][0],un[m]))
