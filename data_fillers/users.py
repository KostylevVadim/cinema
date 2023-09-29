from random import randint
from datetime import date, timedelta
from random import choices
import time    
import random
import string
def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return(rand_string)

def users(cursor,x):
    second_part = ["mail.ru","gmail.com","yandex.ru","yahoo.ru","rambler.ru","hotmail.ru","outlook.com"]
    for i in range(x):
        mail_first = generate_random_string(5)
        mail = mail_first + "@" + second_part[randint(0,len(second_part)-1)]
        user = mail_first = generate_random_string(6)
        pswd = generate_random_string(8)
        date_reg = date(2015,12,12)
        reg_delta = randint(0,2190)
        date_reg = date_reg + timedelta(days=reg_delta)
        ver = randint(0,1)
        delited = randint(0,1)
        sub = randint(0,1)
        print(user, mail, pswd, date_reg, ver, delited, sub)
        cursor.execute("INSERT INTO users (username, mail, passwd, date_reg, verified, deleted, sub) VALUES(%s,%s,%s,%s,%s,%s,%s)",
                       (user,mail,pswd,date_reg,bool(ver),False,bool(sub)))
