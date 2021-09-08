# Creating a file with html text
import requests
urls = ["https://wwww.naver.com/", "https://wwww.python.com/"]
filename = "robots.txt"

for url in urls:
    resp = requests.get(url)
    print("response : ", resp)

##socket.gaierror: [Errno 8] nodename nor servname provided, or not known
