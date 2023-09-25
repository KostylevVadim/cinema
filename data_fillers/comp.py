from random import randint
def comp(cursor): 
    cursor.execute("SELECT id FROM film_series")
    record2 = cursor.fetchall()
    cursor.execute("SELECT id FROM users")
    record1 = cursor.fetchall()
    for i in range(len(record1)):
        any_com = randint(0,2)
        if any_com ==0:
            continue
        else:
            for j in range(any_com):
                how_many = randint(0,len(record2))
                incomp =[]
                for z in range(how_many):
                    x = randint(0,len(record2)-1)
                    if record2[x] in incomp:
                        continue
                    else:
                        incomp.append(record2[x])
                #print(i+1, " ", incomp," ",j+1)
                for m in range(len(incomp)):
                    #print(record1[i][0],record2[m][0],j+1)
                    cursor.execute("INSERT INTO comp (usr_id, film_id, spec) VALUES (%s,%s,%s)",(record1[i][0],record2[m][0],j+1))



