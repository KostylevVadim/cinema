from random import randint

def prese(cursor):
    cursor.execute("SELECT (id) FROM film_series WHERE filorser = True")
    record1 = cursor.fetchall()
    cursor.execute("SELECT (date_real) FROM film_series WHERE filorser = True")
    record2 = cursor.fetchall()
    for i in range(len(record1)):
        cursor.execute("SELECT (id) FROM film_series WHERE filorser = TRUE AND date_real<%s",(record2[i][0],))
        record_temp = cursor.fetchall()
        
        x = record2[i]
        
        print(record1[i])
        for j in range(len(record_temp)):
            y = randint(0,6)
            if(y == 1):
                print("preq - ", record1[i], " seq -", record_temp[j])
                cursor.execute("INSERT INTO film_connection (prec_id, seq_id) VALUES (%s,%s)",(record1[i], record_temp[j]))
                break