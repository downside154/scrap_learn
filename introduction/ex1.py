# Using Requests - Lesson 1

import requests

url = "https://www.python.org"
resp = requests.get(url)

#checking...
print("url : ", url)
print("response : ", resp)

html = resp.text
print(html)
