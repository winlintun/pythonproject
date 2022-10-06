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

# preparing query to create a database

sql = """INSERT INTO notepad (title, content, create_date) VALUES ('title', 'content', '3.2.2022')""";

# create a database
cursor.execute(sql) 
print("Your notebook is entry done.....")

# data = cursor.fetchone()
# print("Connection established to: ", data)

conn.close()

