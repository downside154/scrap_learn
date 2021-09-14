from selenium import webdriver
import time

# 100 stats excel download
def download_bok_stats():

    driver = webdriver.Chrome("../scrapping2/chromedriver")
    driver.implicitly_wait(3)
    driver.get("https://ecos.bok.or.kr/jsp/vis/keystat/#/key")

    excel_dw = driver.find_element_by_css_selector('img[alt="download"]')
    driver.implicitly_wait(3)
    excel_dw.click()

    time.sleep(5)

    driver.close()
    print("Downloading file...")

    return None

# execute function:
download_bok_stats()










