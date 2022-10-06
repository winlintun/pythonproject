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


# title = str(input("Enter The Title: "))
# content = str(input("Enter the content: "))
# create_date = str(input("Enter the date: "))
cursor.execute(""" SELECT * FROM notepad """)


result = cursor.fetchone();
print(result)

# fetching 1 st row from the table,
result = cursor.fetchall();
print("1st row ", result )

conn.close()

