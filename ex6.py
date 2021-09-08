import requests, re 
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp = requests.get(url)
html_src = resp.text

soup = BeautifulSoup(html_src, 'html.parser')

#Using BS4's find_all function,  links is now a list that has a total of 1207 elements stored
links = soup.find_all("a")
print("1. links count : ", len(links))
print("\n")

#links can be sliced
print("2. first 3 links  : ", links[:3])
print("\n")

# using additional parameters to find stuff, re.complie used to see if it contains it
wiki_links = soup.find_all(name="a", href=re.compile("/wiki/"), limit=3)
print("3. first 3 links with /wiki/ : ", wiki_links)
print("\n")

# using class to narrow out search
external_links = soup.find_all(name="a", attrs={'class':'external text'}, limit=3)
print("4. first 3 hyperlink by class : ", external_links)
print("\n")
