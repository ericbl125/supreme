import requests
import urllib
import re
import time
import os.path
import platform
from bs4 import BeautifulSoup

# This could just be the scraper that takes the preview images from the website
# The images are located at
	# https://www.supremenewyork.com/previews/'season+year'/all
# I think I can't go directly to the previews all but I can append /all after finding
	# the previews page

supreme = "https://www.supremenewyork.com/"
mac_path = "/Users/ericbl/Documents/supr_images/images/"
win_path = "C:/Documents/"

def get_soup(url):
	response = requests.get(url)
	html = response.text
	soup = BeautifulSoup(html, "html.parser")
	return soup

def preview_url(soup):
	preview_tag = soup.find_all(href=re.compile("previews"))[0].get("href")
	return  urllib.parse.urljoin(supreme, preview_tag)

def view_all_url(soup):
	view_tag = soup.find_all("a", string="view all")[0].get("href")
	return urllib.parse.urljoin(supreme, view_tag)

def find_file_path():
	if platform.system() == "Windows":
		file_path = win_path
	elif platform.system() == "Darwin":
		file_path = mac_path
	return file_path

def save_image(img_url):
	full_url = urllib.parse.urljoin(supreme, img_url)
	print(img_url[-1])
	full_path = file_path + img_url
	print(full_path)
	#urllib.request.urlretrieve(full_url, )

def find_images(soup):
	imgs = soup.find_all("div", class_="inner-article")
	parsed = list(urllib.parse.urlparse(supreme))
	for img in imgs:
		
		# might want to store the name of the item as well
		#url = img.find_all("a")[0].get("href")
		#img_name = img_url.split('/')[-1]

		# create a database that associates the photo names with the 
			# item names.  Having the item names would make it easier to search
			# inside the store.
		# Also store the class.  it is the second to last index of the url
			# /previews/fallwinter2018/!class!/item_name
			# the store has the classes on the scroll wheel and would make it 
			# easiers to find


		img_src = img.a.img["src"]
		print (img_src)
		img_url = urllib.parse.urljoin(supreme, img_src)
		img_name = img_url.split('/')[-1]

		outpath = os.path.join(mac_path, img_name)
		urllib.request.urlretrieve(img_url, outpath)
		time.sleep(1)


		break	# remove break when it is all
		
# Need to create a function that will create the images directory

		
# gets url for the current product previews	
soup = get_soup(supreme)
preview = preview_url(soup)
time.sleep(1)

# gets the url to view all of the previews page
soup = get_soup(preview)
view = view_all_url(soup)
time.sleep(1)


# Finds and Downloads the Images to a directory
soup = get_soup(view)
find_images(soup)





 ######
 # Possible second Option for saving pictures
 ######
#Get a file-like object from the request and copy it to a file. This will also avoid reading the whole thing into memory at once.
#import shutil
#import requests

#url = 'http://example.com/img.png'
#response = requests.get(url, stream=True)
#with open('img.png', 'wb') as out_file:
#    shutil.copyfileobj(response.raw, out_file)
#del response


