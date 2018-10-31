import sqlite3

# Tables [preview, user_selected]
# Preview fields [ItemName, ImageName, Type, Collaboration, Drop_Date, Price]

# Rewrite this so it is a stand alone class 
# this will manage the database for the Supreme program
# parameters would be which table to access
# use this as an outline https://gist.github.com/goldsborough/c973d934f620e16678bf


class Database:
	def __init__(self, name=None):
		self.conn = None
		self.cursor = None

		if name:
			self.open(name)

	def open(self, name):
		try:
			self.conn = sqlite3.connect(name)
			self.cursor = self.conn.cursor()
		except sqlite3.Error as e:
			print(e)


	def close(self):
		if self.conn:
			self.conn.commit()
			self.cursor.close()
			self.conn.close()

	def __enter__(self):
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.close()

	def createTable(self, name):
		sql = "CREATE TABLE IF NOT EXISTS {} (season text, item text, type text, image text, dropDate text, price real)".format(name)
		self.cursor.execute(sql)

	def write(self, table, data):
		# change into a loop itself
		# will receive a dictionary and then just inserts everything in the dictionary
		sql = "INSERT INTO {0}  ({1}) VALUES ({2});".format(table,columns,data) # -- TODO -- Need to add columns, might need to create a dictionary???
		self.cursor.execute(sql)

	def query(self, table, condition):
		sql = "SELECT FROM {0} WHERE {1}".format(table, condition)
		self.cursor.execute(sql)
		rows = self.cursor.fetchall()
		return rows





	
