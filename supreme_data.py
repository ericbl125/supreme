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
			self.cursor = self.conn.cursor
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
		sql = "CREATE TABLE {} (season text, item text, type text, image text, drop text, price real)".format(name)
		self.execute(sql)

	def write(self, table, data):
		sql = "INSERT INTO {0} ({1}) VALUES ({2});".format(table,columns,data)
		self.cursor.execute(sql)

	def query(self, table, condition):
		sql = "SELECT FROM {0} WHERE {1}".format(table, condition)
		self.cursor.execute(sql)
		rows = self.cursor.fetchall()
		return rows

	


	def insert_image():
		self.execute("INSERT INTO SupremeItemList VALUES(?, ?, ?, ?, ?)") # insert values after the comma

	def search_image_name(name):
		return self.execute("SELECT FROM SupremeItemList WHERE imageName = ?", name)

	




	
