import psycopg2
from psycopg2 import Error




class ContextManager(): 
    def __init__(self, connection, cursor):
        self.connection = connection
        self.cursor = cursor
          
    def __enter__(self): 
        return self.cursor
      
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type is not None:
            raise Error('Problem with database')
        self.cursor.close()
        self.connection.commit()
        print('Connection Closed')

connection = psycopg2.connect(user="postgres",
                                  password="123",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="cinema")


with ContextManager(connection, connection.cursor()) as cursor:
    cursor.execute('SELECT * FROM users_usr LIMIT 1')
    a = cursor.fetchall()
    print(a)
    


    
    








