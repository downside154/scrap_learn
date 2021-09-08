# Saving images on web into local PC
import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp = requests.get(url)
html_src = resp.text

soup = BeautifulSoup(html_src, 'html.parser')

target_img = soup.find(name='img', attrs={'width':'1000'})
print("HTML Element: ", target_img)

target_img_src = target_img.get('src')
print("Image src: ", target_img_src)

target_img_resp = requests.get('http:' + target_img_src)
out_file_path = "./output/download_image"
# ./output directory must exist, the file will be saved as download_image
print("response: ", target_img_resp)


with open(out_file_path, 'wb') as outfile:
    outfile.write(target_img_resp.content)
    print("Image file has been saved")

