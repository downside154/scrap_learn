from selenium import webdriver
from decouple import config 

# using selenium for dynamic web scape part

driver = webdriver.Chrome('../scrapping2/chromedriver')
driver.implicitly_wait(5)
driver.get("https://www.danawa.com/")

login = driver.find_element_by_css_selector('#danawa_menubar > div.main-header__user > div:nth-child(5) > a')
login.click()
driver.implicitly_wait(5)

danawa_id = config('DANAWA_ID') # find enviromental variables
danawa_pw = config('DANAWA_PW') # find enviromental variables

driver.find_element_by_id('danawa-member-login-input-id').send_keys(danawa_id)
driver.implicitly_wait(2)
driver.find_element_by_name('password').send_keys(danawa_pw)
driver.implicitly_wait(2)
driver.find_element_by_css_selector('button.btn_login').click()

#scrapping wish list as HTML
wishlist = driver.find_element_by_css_selector('#danawa_menubar > div.main-header__user > div:nth-child(4) > a').click()
driver.implicitly_wait(2)
html_src = driver.page_source
driver.close()
print("what is this:", html_src[:500])
print("\n")

from bs4 import BeautifulSoup
import re

soup = BeautifulSoup(html_src, 'html.parser')
wish_table = soup.select('table[class="tbl wish_tbl"]')[0]
wish_items =wish_table.select('tbody tr')

for item in wish_items:
    title = item.find('div', {'class':'tit'}).text
    price = item.find('span', {'class':'price'}).text
    link = item.find('a', href=re.compile('prod.danawa.com/info/')).get('href')
    print("title: ", title)
    print("price: ", price)
    print("link: ", link)
    print("\n")






