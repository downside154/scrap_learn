import requests
from bs4 import BeautifulSoup

# USING CSS Selectors PART 2

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp = requests.get(url)
html_src = resp.text
soup = BeautifulSoup(html_src, 'html.parser')

#soup's select is similar to find_all() method. 
#send the tag's name as its parameters and it returns all elements with the tag as a list.
#used len() to find total sum: 1207
links = soup.select('a')
print("length of links: ", len(links))
print("\n")

#can be sliced as it is a list
print("sliced top 3 links : ", links[:3])
print("\n")

#search for a tags with class exactly as "external text" in that order
external_links = soup.select('a[class="external text"]')
print("sliced top 3 exlinks : ", external_links[:3])
print("count exlinks: ", len(external_links))
print("\n")

# use "#" to search for id's
id_selector = soup.select('#siteNotice')
print("id selector : ", id_selector)
print("\n")

# "#" can be used with tags
id_selector2 = soup.select('div#siteNotice')
print("id selector 2 : ", id_selector2)
print("\n")

# will return an empty list as this element does not exist
id_selector3 = soup.select('p#siteNotice')
print("id selector 3 : ", id_selector3)
print("\n")

# class searches work by using "."
class_selector = soup.select('.mw-headline')
print("class selector : ", class_selector)
print("\n")

# this can also work with tags
class_selector2 = soup.select('span.mw-headline')
print("class selector 2 : ", id_selector2)
print("\n")