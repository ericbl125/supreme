from preview import preview
from Database import Database


def main():
	prev = preview()
	print ("Complete")
	#***********
	# -- TODO -- Change the format of the data to being a dictionary; 
		# it will be column with the corresponding index of that reference being the order of insertion
	#***********

	
	#	data = {Season: [fallwinter2018] Item: [wool-beanie, bomber-jacket-a] Type:[hat, jacket] Image: [acb.jpg, xyz.jpg] dropDate: [None, None] price: [None, None]}
	
	data = prev.data
	print (data)


	#***********
	# -- TODO -- Implement the database entry here or Within preview.py
	#***********
	supreme = Database("SupremeData.db")
	supreme.createTable("PreviewItems")
	#with Database() as supreme:
	for info in data:
		#supreme.createTable("PreviewItems")
		supreme.write("PreviewItems", info)

	

	# I think entering the data from within main would be easier to implement than within preview
	# It will be slower running it from within Main but easier to handl implementing

if __name__ == "__main__" :
	main()
