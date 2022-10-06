import psycopg2


# establishing the connection
conn = psycopg2.connect(
	database = 'mydb',
	user = 'postgres',
	password = 'toor',
	host = 'localhost',
	port = '5432'
	)

conn.autocommit = True

# create a cursor object using the cursor() method
cursor = conn.cursor()

# preparing query to create a database
sql = '''CREATE database notepad''';

# create a database
cursor.execute(sql)
print("Database created successfully.....")

# cursor.execute('select version()')

data = cursor.fetchone()
print("Connection established to: ", data)

conn.close()

