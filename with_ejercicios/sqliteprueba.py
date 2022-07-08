import sqlite3

class SQLite:
    
    def __init__(self):
        
        self.connection = sqlite3.connect('Agenda.db') 

    def __enter__(self):
        
        cur = self.connection.cursor()
        
    
    def __exit__(self, type, value, traceback):
        
        self.connection.commit()
        self.connection.close()
  
    


