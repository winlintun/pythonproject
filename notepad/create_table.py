import psycopg2
from datetime import datetime


conn = psycopg2.connect(
	database = 'notepad',
	user = 'postgres',
	password = 'toor',
	host = 'localhost',
	port = '5432'
	)

conn.autocommit = True

cursor = conn.cursor()

sql = '''CREATE TABLE notepad (
title VARCHAR(255) NOT NULL,
content TEXT,
create_date DATE NOT NULL DEFAULT CURRENT_DATE
)''';

cursor.execute(sql)

print("Table created successfully.....")

conn.close()
