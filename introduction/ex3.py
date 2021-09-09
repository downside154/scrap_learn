import requests
from bs4 import BeautifulSoup
#Using BS4 
url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp = requests.get(url)
html_src = resp.text

soup = BeautifulSoup(html_src, 'html.parser')
print(type(soup))

print("title element: ", soup.title)
print("title tag name:", soup.title.name)
print("title tag string:", soup.title.string)
