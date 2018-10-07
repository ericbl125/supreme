# preview class

# methods
	# get soup for supreme home page
	# get soup for preview page
	# get soup to view all preview items
	# find images
	# create file path

import requests
import urllib
import re
import os.path
import time
from bs4 import BeautifulSoup

class preview:
	def __init__(self):

		self.supreme = "https://www.supremenewyork.com/"
		self.data = []

		soup = self.get_soup(self.supreme)
		preview = self.find_url(soup, "preview")

		self.season = self.set_season(soup)
		time.sleep(.5)

		# gets the url to view all of the previews page
		soup = self.get_soup(preview)
		view = self.find_url(soup, "view")
		time.sleep(.5)

		# Finds and Downloads the Images to a directory
		soup = self.get_soup(view)
		self.find_images(soup)

	def get_soup(self, url):
		response = requests.get(url)
		html = response.text
		soup = BeautifulSoup(html, "html.parser")
		return soup

	def set_season(self, soup):
		season = soup.find_all("a", string=re.compile("preview"))[0].get("href")
		return season.split('/')[-1]

	def find_url(self, soup, str):
		view_tag = soup.find_all("a", string=re.compile(str))[0].get("href")
		return urllib.parse.urljoin(self.supreme, view_tag)

	def find_images(self, soup):
		imgs = soup.find_all("div", class_="inner-article")
		#parsed = list(urllib.parse.urlparse(supreme))

		for img in imgs:

			info = []
			url = img.find_all("a")[0].get("href")
			item_name = url.split('/')[-1]	# gets the item's name
			item_type = url.split('/')[3]	# gets the item's type

			img_src = img.a.img["src"]
			src_url = urllib.parse.urljoin(self.supreme, img_src)
			img_name = src_url.split('/')[-1]	

			info.append(self.season)
			info.append(item_name)
			info.append(item_type)
			info.append(img_name)

			self.data.append(info)

			#*************
			# --- TODO --- Insert data into the database
			#*************

			user_path = self.get_path();
			outpath = os.path.join(user_path, img_name)
			urllib.request.urlretrieve(src_url, outpath)
			time.sleep(.25)

			# break 	# This break is here for testing

	def get_path(self):
		user_path =  os.path.join(os.path.expanduser("~"), "Documents", "Supreme", "Images") # sets according to users computer pathz
		if not os.path.isdir(user_path):
			os.makedirs(user_path)
		return user_path


