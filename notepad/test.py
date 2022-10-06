import psycopg2

def create_databases():
	conn = psycopg2.connect(
	database = 'mydb',
	user = 'postgres',
	password = 'toor',
	host = 'localhost',
	port = '5432'
	)

	conn.autocommit = True

	cursor = conn.cursor()

	sql = 'CREATE DATABASE notepad';

	try:
		cursor.execute(sql)
		print("Successfully Database Create....")
	except:
		print("Your Database is already exists..")


	conn.close()



def create_table():

	conn = psycopg2.connect(
	database = 'mydb',
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

	try:
		cursor.execute(sql)
		print("Table created successfully.")
	except:
		print("Your table is already exists...")

	conn.close()


def data_insert_into():
	conn = psycopg2.connect(
	database = 'mydb',
	user = 'postgres',
	password = 'toor',
	host = 'localhost',
	port = '5432'
	)

	conn.autocommit = True

	cursor = conn.cursor()

	sql = """INSERT INTO notepad (title, content, create_date) VALUES (%s, %s, %s)"""

	title = input("title: ")
	content = input("content: ")
	date_time = input("time: ")
	data = (title, content, date_time)

	try:
		cursor.execute(sql, data)
		print("Data entry is successfully....")
	except(Exception, psycopg2.Error) as error:
		print("Something wrong....", error)

	conn.close()



def show_table_data():

	conn = psycopg2.connect(
	database = 'mydb',
	user = 'postgres',
	password = 'toor',
	host = 'localhost',
	port = '5432'
	)

	conn.autocommit = True

	cursor = conn.cursor()

	cursor.execute('SELECT * FROM notepad')

	result = cursor.fetchall()
	#print('id', '\t', 'title', '\t', 'content', '\t \t', 'date', '\t \n')
	for x in result:
		print(x[0], '\t', x[1], '\t', x[2], '\t \t', x[3], '\t')


	conn.close()


def delete_data():

	conn = psycopg2.connect(
	database = 'mydb',
	user = 'postgres',
	password = 'toor',
	host = 'localhost',
	port = '5432'
	)

	conn.autocommit = True

	cursor = conn.cursor()

	show_table_data()

	try:
		sql_delete = """ DELETE FROM notepad WHERE id = %s """
		data = input("Enter id number: ")
		cursor.execute(sql_delete, data)
		count = cursor.rowcount
		print(count, "Record delete successfully...")
	except(Exception, psycopg2.Error) as error:
		print("Error in Deleting data", error)

	cursor.close()


def update_data():
	conn = psycopg2.connect(
	database = 'mydb',
	user = 'postgres',
	password = 'toor',
	host = 'localhost',
	port = '5432'
	)

	conn.autocommit = True

	cursor = conn.cursor()

	show_table_data()

	user = int(input(""" 
	1. title update
	2. content update
	3. date update
	>: """))

	if user == 1:
		try:
			sql_update_title = """ UPDATE notepad SET title = %s WHERE id = %s """
			title = input("Enter title rename: ")
			data = input("Enter id number: ")
			cursor.execute(sql_update_title, (title,data))
			count = cursor.rowcount
			print(count, "Title record update successfully...")
		except(Exception, psycopg2.Error) as error:
			print("Error in updating data", error)

	elif user == 2:
		try:
			sql_update_content = """ UPDATE notepad SET content = %s WHERE id = %s """
			content = input("Enter content: ")
			data = input("Enter id number: ")
			cursor.execute(sql_update_content, (content, data))
			count = cursor.rowcount
			print(count, "Content record update successfully...")
		except(Exception, psycopg2.Error) as error:
			print("Error in updating data", error)
	elif user == 3:
		try:
			sql_update_date = """ UPDATE notepad SET create_date = %s WHERE id = %s """
			date_time = input("Enter title rename: ")
			data = input("Enter id number: ")
			cursor.execute(sql_update_date, (date_time, data))
			count = cursor.rowcount
			print(count, "Date record update successfully...")
		except(Exception, psycopg2.Error) as error:
			print("Error in updating data", error)

	else:
		print("Something wrong....")


	conn.close()









if __name__ == '__main__':

	program_exit = ''

	while program_exit != '100':

		print("""
			--------------------------------------
				Welcome My Database Program
			--------------------------------------
		1. Create Databases
		2. Create Table in Databases
		3. Data insert in Table
		4. Show Data in Table
		5. Update data

		9. Delete data
		0. Existing Program
			""")
		user = int(input("Enter Options: "))

		if user == 1:
			create_databases()
		elif user == 2:
			create_table()
		elif user == 3:
			data_insert_into()
		elif user == 4:
			show_table_data()
		elif user == 5:
			update_data()

		elif user == 9:
			delete_data()
		elif user == 0:
			program_exit = '100'
			print("Thank You...Bye!")

		else:
			print("Wrong Options....\n Plz Tryagain!")
