from random import randint
from datetime import date, timedelta
def review(cursor, n):
    cursor.execute("SELECT * FROM users")
    record1 = cursor.fetchall()
    cursor.execute("SELECT * FROM film_series")
    record2 = cursor.fetchall()   
    cursor.execute('SELECT MIN(id) FROM users')
    min_user = cursor.fetchall()
    cursor.execute('SELECT MIN(id) FROM film_series')
    min_film = cursor.fetchall()
    #print(min_user, min_film)
    review_firstpart = ["Very nice film. ", "Good film. ", "Normal film. ", "Not good film. ", "Bad film. ", "Awful film. "]
    review_secondpart = ["I learned a lot", "I love it for charecters", "I really wnt a new part", "It is just nice", "Tells a lot about our time", 
                        "Would kinly", "It won't make you boring", "Lovely film", "Really hate it", "Just ordinary","For other people",
                        "I ve lost time", "I saw it when i was a child", " Kono Dio da", "Dialogs are perfect", "Poor Tarnished",
                        "Upon my name as Godfrey", "haiiii","Crocodile","Shinshila","You are good", "AAAAAAAA","would you kindly",
                        "You are wizard", "I m Blaidd", "Now i watch as worrior", "Nice Nice very nice", "Yeeeee","I know place from film",
                        "Actually not bad", "Worth it", "Now to the reallity","Godzilla is better","Trees are perfect here","I just love cinema",
                        "Cars here are best part", "It changed my life"]
    for i in range(n):
        q = review_firstpart[randint(0,len(review_firstpart)-1)]
        a = q + review_secondpart[randint(0,len(review_secondpart)-1)]
        rate = 0
        #print(a)
        if q ==review_firstpart[0]:
            rate = randint(9,10)
        if q ==review_firstpart[1]:
            rate = randint(7,8)
        if q ==review_firstpart[2]:
            rate = randint(5,6)
        if q ==review_firstpart[3]:
            rate = randint(3,4)
        if q ==review_firstpart[4]:
            rate = randint(1,2)
        if q ==review_firstpart[5]:
            rate = 0
        #print('Second',rate)
        
        inner_rate = randint(-100,100)
        users = randint(min_user[0][0],min_user[0][0]+len(record1)-1)
        film = randint(min_film[0][0],min_film[0][0]+len(record2)-1)
        #print(users, film)
        #date_reg = date(2015,12,12)
        cursor.execute("SELECT date_reg FROM users WHERE users.id = %s",((users,)))
        record3 = cursor.fetchall()
        date_reg = record3[0][0]
        #print(record3)
        cursor.execute("SELECT verified FROM users WHERE id = %s",((users,)))
        
        record4 = cursor.fetchall()

        #print(record3, record4)
        
        reg_delta = randint(0,1190)
        date_reg = date_reg + timedelta(days=reg_delta)
        
        var = record4[0][0]
        print(a , " ", rate, " ", inner_rate, " ",film, " ", users, " ",date_reg, " ", var)
        cursor.execute("INSERT INTO review (rate, txt, review_rate, dat, usr_id, film_id, varified) VALUES (%s,%s,%s,%s,%s,%s,%s)",
         (rate,a, inner_rate, date_reg, users, film, var))