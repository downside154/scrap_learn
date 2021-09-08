import requests

urls = 'https://wwww.naver.com/'
filename = 'robots.txt'


file_path = urls + filename
print(file_path, type(file_path))

resp = requests.get(urls)
print(resp.text)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


resp1 = requests.get(file_path, headers=headers)
print(resp1)
    # resp = requests.get(file_path).text
    # print(resp)
    # print("\n")