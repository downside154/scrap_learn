import requests
from bs4 import BeautifulSoup

# USING CSS Selectors

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp = requests.get(url)
html_src = resp.text
soup = BeautifulSoup(html_src, 'html.parser')


#Using CSS selectors
subway_image = soup.select('#mw-content-text > div.mw-parser-output > div.center\
 > div > div > a > img')
# get its CSS selector from the browser's selector tools:
#   right-click element > "copy" > "copy selector"

print("subway image : ", subway_image)
print("\n")

print("0th index image : ", subway_image[0])
print("\n")
# it can contain a list of elements, so use indexes to find

subway_image2 = soup.select('tr > td > a > img')
print("image2 : ", subway_image2)