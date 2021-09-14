from selenium import webdriver
from bs4 import BeautifulSoup
import time

# search stats with keyword and save as CSV
def download_bok_stats_by_keyword():
    
    item_found = 0
    while not item_found:

        #reset search keyword
        keyword = ""
        while len(keyword) == 0:
            keyword = str(input("검색어를 입력하세요 : "))
        # webdriver run
        driver = webdriver.Chrome("../scrapping2/chromedriver")
        driver.implicitly_wait(4)
        driver.get("https://ecos.bok.or.kr/jsp/vis/keystat/#key")
        time.sleep(5) # delays execution for 5 secs
        
        # find_element - non scriptable, non iterable WebElement
        # # find_elements - list of webElements
        items1 = driver.find_elements_by_css_selector('a[class="ng-binding"]')
        items2 = driver.find_elements_by_css_selector('a[class="a-c1-list ng-binding"]')
        items3 = driver.find_elements_by_css_selector('a[class="a-c4-list ng-binding"]')
        driver.implicitly_wait(5)

        items = items1[1:] + items2 + items3

        for idx, item in enumerate(items):
            if keyword in item.text:
                print(f"검색어 '{keyword}'에 매칭되는 '{item.text}' 통계지표를 검색 중... ")
                item.click()
                item_found = 1
                time.sleep(5)
                break
            elif idx == (len(items)-1):
                print(f"검색어 '{keyword}'에 대한 통계지표가 존재하지 않습니다. ")
                driver.close()
                continue
            else:
                pass

    # 검색결과 로딩 html 웹 페이지를 파싱 - 통계지표 테이블(표) 양식 정리
    html_src = driver.page_source
    soup = BeautifulSoup(html_src, 'html.parser')
    driver.close()

    table_items = soup.find_all('td',{'class':'ng-binding'})
    date = [t.text for i, t in enumerate(table_items) if i % 3 == 0]
    value = [t.text for i, t in enumerate(table_items) if i % 3 == 1]
    change = [t.text for i, t in enumerate(table_items) if i % 3 == 2]

    #save as CSV file
    result_file = open(f'./data/bok_statistics_{keyword}.csv', 'w')
    for i in range(len(date)):
        result_file.write(f'{date[i]}, {value[i]}, {change[i]}')
        result_file.write('\n')
    
    result_file.close()
    print(f"Saved csv for keyword '{keyword}' ")
    return date, value, change


#executing function - 'CS수익률' 통계지표를 별도로 검색, CSV 파일로 저장
result = download_bok_stats_by_keyword()
print(result)
