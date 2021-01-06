#create a data base using connect function and put the refrence in conn var
import sqlite3
from sqlite3 import Error
def create_connection(students):
    conn = None
    try:
        conn = sqlite3.connect(students)
        print(sqlite3.version)
        return conn
    except Error as e:
        print (e)
    finally:
        if conn:
         conn.close()

create_connection(r"C:\sqlite\db\pythonsqlite.db")