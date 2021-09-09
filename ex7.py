import requests
from bs4 import BeautifulSoup

# USING CSS Selectors

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp = requests.get(url)
html_src = resp.text
soup = BeautifulSoup(html_src, 'html.parser')


#Using CSS slectors
subway_image = soup.select('#mw-content-text > div.mw-parser-output > div.center\
 > div > div > a > img')
print("subway image : ", subway_image)
print("\n")
print("0th index image: ", subway_image[0])
print("\n")


subway_image2 = soup.select('tr > td > a > img')
print(subway_image2[1])