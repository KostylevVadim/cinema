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