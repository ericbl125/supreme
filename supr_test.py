import requests
import urllib

from bs4 import BeautifulSoup

supreme = "https://www.supremenewyork.com/"
# loop through the li
# it is the second one
response = requests.get(supreme)
html = response.text
soup = BeautifulSoup(html, "html.parser")

ultag = soup.select("ul")
preview_tag = soup.select("li")[1]
preview_link = lookbook.get("href")
preview = urllib.parse.urljoin(supreme, preview_link)

response = requests.get(preview)
html = response.text
soup = BeautifulSoup(html, "html.parser")


print(lookbook)


#Get a file-like object from the request and copy it to a file. This will also avoid reading the whole thing into memory at once.
#import shutil
#import requests

#url = 'http://example.com/img.png'
#response = requests.get(url, stream=True)
#with open('img.png', 'wb') as out_file:
#    shutil.copyfileobj(response.raw, out_file)
#del response


