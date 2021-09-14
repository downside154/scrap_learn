from selenium import webdriver
from decouple import config 

driver = webdriver.Chrome('../scrapping2/chromedriver')
driver.implicitly_wait(5)
driver.get("https://www.danawa.com/")


login = driver.find_element_by_css_selector('#danawa_menubar > div.main-header__user > div:nth-child(5) > a')
print("HTML ELEMENT : ", login)
print(" Tag name : ", login.tag_name )
print("string : ", login.text )
print(" href element: ", login.get_attribute('href') )


login.click()
driver.implicitly_wait(5)

danawa_id = config('DANAWA_ID') # find enviromental variables
danawa_pw = config('DANAWA_PW') # find enviromental variables

driver.find_element_by_id('danawa-member-login-input-id').send_keys(danawa_id)
driver.implicitly_wait(2)
driver.find_element_by_name('password').send_keys(danawa_pw)
driver.implicitly_wait(2)

driver.find_element_by_css_selector('button.btn_login').click()