import psycopg2
from datetime import date, timedelta

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

    def add_user(self, username: str, mail: str, passwd: str, verified: bool, sub: bool):
        d = date.today()
        self.__cursor.execute("INSERT INTO users (username, mail, passwd, date_reg, verified, deleted, sub) VALUES(%s,%s,%s,%s,%s,%s,%s)",
                       (username,mail,passwd,d,verified,False,sub))
    
    def delete_user(self, username):
        self.__cursor.execute("UPDATE users SET deleted=True WHERE username=%s", (username,))