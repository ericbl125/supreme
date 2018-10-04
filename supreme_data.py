import sqlite3

class DataConnect(sqlite3.Connection):
	def cursor(self):
		return super(DataConnect, self).cursor(data)

	def close_db():
		connection.close()

	def commitDB():
		connection.commit();

class data(sqlite3.Cursor):
	def create_image_table(self):
		self.execute("CREATE TABLE SupremeItemList (season text, itemName text, imageName text, dropDate text, price real)")

	def insert_image():
		self.execute("INSERT INTO SupremeItemList VALUES(?, ?, ?, ?", ) # insert values after the comma

	def search_image_name(name):
		return self.execute("SELECT FROM SupremeItemList WHERE imageName = ?", name)

	#conn = sqlite3.connect("superemeData.db", factory=data.DataConnect)
	
