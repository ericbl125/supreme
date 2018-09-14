import requests
import urllib
import re

from bs4 import BeautifulSoup

# This could just be the scraper that takes the preview images from the website
# The images are located at
	# https://www.supremenewyork.com/previews/'season+year'/all
# I think I can't go directly to the previews all but I can append /all after finding
	# the previews page

supreme = "https://www.supremenewyork.com/"

def navigate_to_preview(supreme):
	response = requests.get(supreme)
	html = response.text
	soup = BeautifulSoup(html, "html.parser")
	preview_tag = soup.find_all(href=re.compile("previews"))[0].get("href")
	return  urllib.parse.urljoin(supreme, preview_tag)

def view_all(soup):
	view_all = soup.find_all("a", string="view all")[0]
	print(view_all)
	atag = view_all.get("href")
	print(atag)


preview = navigate_to_preview(supreme)
print(preview)
response = requests.get(preview)
html = response.text
soup = BeautifulSoup(html, "html.parser")

view_all(soup)





#Get a file-like object from the request and copy it to a file. This will also avoid reading the whole thing into memory at once.
#import shutil
#import requests

#url = 'http://example.com/img.png'
#response = requests.get(url, stream=True)
#with open('img.png', 'wb') as out_file:
#    shutil.copyfileobj(response.raw, out_file)
#del response


