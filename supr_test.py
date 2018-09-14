import requests
import urllib
import re

from bs4 import BeautifulSoup

supreme = "https://www.supremenewyork.com/"
# loop through the li
# it is the second one
response = requests.get(supreme)
html = response.text
soup = BeautifulSoup(html, "html.parser")
preview_tag = soup.find_all(href=re.compile("previews"))[0].get("href")
preview = urllib.parse.urljoin(supreme, preview_tag)

response = requests.get(preview)
html = response.text
soup = BeautifulSoup(html, "html.parser")


print(preview_tag)
print(preview)



#Get a file-like object from the request and copy it to a file. This will also avoid reading the whole thing into memory at once.
#import shutil
#import requests

#url = 'http://example.com/img.png'
#response = requests.get(url, stream=True)
#with open('img.png', 'wb') as out_file:
#    shutil.copyfileobj(response.raw, out_file)
#del response


