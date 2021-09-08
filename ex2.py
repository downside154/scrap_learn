# Creating a file with html text
import requests
urls = ["https://wwww.naver.com/", "https://wwww.python.com/"]
filename = "robots.txt"


for url in urls:
    file_path = url + filename
    print("file_path", file_path)
    resp = requests.get(file_path)
    print("response : ", resp.text)
    print("\n")

##socket.gaierror: [Errno 8] nodename nor servname provided, or not known
