

import sqlite3


class Database:

    
    def __init__(self, name='/Users/evrard/Documents/alino/db/gescom.db'):
        
        self.conn = None
        self.cursor = None
        self.open(name)

    
    def open(self,name):
        
        try:
            self.conn = sqlite3.connect(name);
            self.cursor = self.conn.cursor()

        except sqlite3.Error as e:
            print("Error connecting to database!")

    def close(self):
        
        if self.conn:
            self.conn.commit()
            self.cursor.close()
            self.conn.close()


    def __enter__(self):
        
        return self

    def __exit__(self,exc_type,exc_value,traceback):
        
        self.close()


    def get(self,table,columns,limit=None):

        query = "SELECT {0} from {1};".format(columns,table)
        self.cursor.execute(query)

        # fetch data
        rows = self.cursor.fetchall()

        return rows[len(rows)-limit if limit else 0:]


    def getLast(self,table,columns):
        
        return self.get(table,columns,limit=1)[0]

    def query(self,sql):
        self.cursor.execute(sql)
        self.conn.commit()
        return self.cursor

    def getquery(self,sql,values):
        self.cursor.execute(sql,values)
        return self.cursor

    def delquery(self,sql,values):
        self.cursor.execute(sql,values)
        self.conn.commit()

    def update(self,sql,values):
        self.cursor.execute(sql,values)
        self.conn.commit()

