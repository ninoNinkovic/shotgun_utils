import sg_utils
import sqlite3
import requests

db_name = 'sg_user_02.db'
name = "users"

conn = sqlite3.connect(db_name)
conn.text_factory = str
db = conn.cursor()

def create_table(name):
	db.execute('''CREATE TABLE "%s"
		(id int, 
		firstname text, 
		lastname text, 
		email text, 
		phone text, 
		portfolio_url text,
		photo blob)''' % name)

def list_tables(name):
	db.execute('''SELECT name FROM "%s" WHERE type='table';''' % name)
	print(db.fetchall())

def insert(data):
	db.execute('''INSERT INTO users VALUES (?,?,?,?,?,?,?)''', data)

def add_sg_users():

	# Add all user from SG database to loacal DB.
	users = sg_utils.list_users()
	for user in users:

		# Get photo as a binary
		if user["image"] != None:
			r = requests.get(user["image"])
			user_image = buffer(r.content)
		else:
			user_image = None

		
		
		data = [user["id"],
				user["firstname"],
				user["lastname"],
				user["email"],
				user["sg_phone"],
				user["sg_portfolio__url_"],
				user_image]
		insert(data)

		print user["firstname"], "created"

# create_table(name)

add_sg_users()	

conn.commit()
conn.close()