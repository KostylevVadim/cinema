import psycopg2
from datetime import date, timedelta
from psycopg2 import Error
class Cinema_worker:
    
    def __init__(self, connection ,cursor):
        self.__connection = connection
        self.__cursor = cursor
    
    def __new__(cls, connection, cursor):
        if 'cinema' in str(connection):
            return super().__new__(cls)
    
    def __str__(self) -> str:
        return str(self.__connection)
    
    def add_film_or_series(self, filmname: str, date_real: str, age, filorser: bool, cost, season = 0, series = 0):
        d = date_real.split('.')
        date_real = date(int(d[2]),int(d[1]),int(d[0]))
        if filorser == True:
            self.__cursor.execute("INSERT INTO film_series (film_name,date_real,age,filorser,cost) VALUES(%s,%s,%s,%s,%s)",(
                filmname, date_real, age, filorser, cost
            ))
        else:
            self.__cursor.execute("INSERT INTO film_series (film_name,date_real,age,filorser,cost,season,series) VALUES(%s,%s,%s,%s,%s,%s,%s)",
            (filmname,date_real,age,filorser,cost,season,series))

    def __uniq_password(self, passwd: str):
        self.__cursor.execute("SELECT COUNT(*) FROM users WHERE passwd=%s",(passwd,))
        x = self.__cursor.fetchall()
        
        if x[0][0]>0:
            return False
        return True
    def __uniq_username(self, username:str):
        self.__cursor.execute("SELECT COUNT(*) FROM users WHERE username=%s",(username,))
        x = self.__cursor.fetchall()
        if x[0][0]>0:
            return False
        return True
    def __uniq_mail(self, mail: str):
        self.__cursor.execute("SELECT COUNT(*) FROM users WHERE mail=%s",(mail,))
        x = self.__cursor.fetchall()
        
        if x[0][0]>0:
            return False
        return True    
    def __is_valid_mail(self, mail:str):
        end = mail.split('@')[-1]
        
        if end in ["mail.ru","gmail.com","yandex.ru","yahoo.ru","rambler.ru","hotmail.ru","outlook.com"]:
            return True
        raise Error('Invalid mail')
    
    def add_user(self, username: str, mail: str, passwd: str, verified: bool, sub: bool):
        d = date.today()
        if self.__is_valid_mail(mail) is not True:
            raise Error('Mail invalid')
        
        if self.__uniq_mail(mail) == False or self.__uniq_password(passwd)==False or self.__uniq_username(username)==False:
            
            raise Error('Not uniq info')
        self.__cursor.execute("INSERT INTO users (username, mail, passwd, date_reg, verified, deleted, sub) VALUES(%s,%s,%s,%s,%s,%s,%s)",
                       (username,mail,passwd,d,verified,False,sub))
        return 'added'
    
    def add_person(self, fullname, born_date, death_date, ful_bio):
        self.__cursor.execute("INSERT INTO person (per_name, birth_date, death_date, bio) VALUES(%s,%s,%s,%s)",
            (fullname,born_date, death_date,ful_bio))
    def enter_your_command(self, string: str, variebles = (0,)):
        self.__cursor.execute(string, variebles)
        x=string.split(" ")
        if x[0] == "SELECT":
            y = self.__cursor.fetchall()
            return y
        
    def restore_user(self, username:str):
        self.__cursor.execute("UPDATE users SET deleted=False WHERE username=%s", (username,))
    def delete_user(self, username):
        self.__cursor.execute("UPDATE users SET deleted=True WHERE username=%s", (username,))