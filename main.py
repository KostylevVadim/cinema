import psycopg2

from cinema_worker import Cinema_worker
from context_manager import ContextManager

    
    


        
        

connection = psycopg2.connect(user="postgres",
                                  password="123",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="cinema")


with ContextManager(connection, connection.cursor()) as cursor:
    x = Cinema_worker(connection, cursor)
    x.delete_user('wkgprd')
    
    


    
    








