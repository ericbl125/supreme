import sqlite3


# Database create a new seasons
connection = sqlite3.connect("supreme_data.db")
cursor = connection.cursor()

def create_image_table():
	cursor.execute("CREATE TABLE SupremeItemList "
		+ "(itemName text, imageName text, dropDate text, price real ")
	cursor.commit();

def insert_image():
	cursor.execute("INSERT INTO SupremeItemList VALUES(?, ?, ?, ?", ) # insert values after the comma


connection.close()