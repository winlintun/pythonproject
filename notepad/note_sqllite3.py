"""
pip install pysqlite3 

"""

import sqlite3
from sqlite3 import Error

def create_new_database(db_file):
    ''' create a database connection to SQLite database '''
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except (Exception, Error) as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    print("""
          1. Default create
          2. give the database name
          """)
    user = input("Enter Options: ")
    if user == '1':
        create_new_database(r'name.db') 
    elif user == '2':
        print("Database name: Default.db")
        name = input('Database name: ')
        if name.endswith('.db'):
            create_new_database(name)
        else:
            print("Wrong Database Name!\n Please confirm your .db name")
    else:
        print("Wrong Option!!!!\n Try Again.")
        

        










# conn = sqlite3.connect('note.db')
# print("Opened database successfully")

# conn.execute('''CREATE TABLE notepad
#              (ID INT PRIMARY KEY NOT NULL,
#              TITLE VARCHAR(255) NOT NULL,
#              CONTENT TEXT,
#              CREATE_DATE DATE);''')
# print("Table created successfully.")
# conn.close()
# print("Database are close now!")