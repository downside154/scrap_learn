# Google News Crawling Part 2
from bs4 import BeautifulSoup
import urllib
import requests

#/search? is disallowed by www.google.com
# will use /? instead 

# Google News Search (Search: 파이썬 = %ED%8C%8C%EC%9D%B4%EC%8D%AC)
base_url = 'https://news.google.com'
keyword_input = '파이썬'
keyword = urllib.parse.quote(keyword_input)
print("search in url: ", keyword)

search_url = base_url + "/?q=" + keyword + "&hl=ko&gl=KR&ceid=KR%3Ako"
resp = requests.get(search_url)
html_src = resp.text
soup = BeautifulSoup(html_src, 'html.parser')


###################################################
### Combining all into a news clipping function ###
###################################################

def google_news_clipping_keyword(keyword, limit=5):

    keyword = urllib.parse.quote(keyword_input)
    search_url = base_url + "/?q=" + keyword + "&hl=ko&gl=KR&ceid=KR%3Ako"

    resp = requests.get(search_url)
    html_src = resp.text
    soup = BeautifulSoup(html_src, 'html.parser')

    news_items = soup.select('div[class="xrnccd"]')

    links= []; titles=[];  agencies=[]; reporting_dates=[];reporting_times=[];
    
    for item in news_items[:limit]:
        #link        
        link = item.find('a', attrs={'class':'VDXfz'}).get('href').split(".")[1]
        news_link = base_url + link
        links.append(news_link)

        #title
        news_title = item.find('a', attrs={'class':'DY5T1d'}).getText()
        titles.append(news_title)
        
        #agency
        news_agency = item.find('a', attrs={'class':'wEwyrc AVN2gc uQIVzc Sksgp'}).text
        agencies.append(news_agency)

        #time
        news_reporting = item.find('time', attrs={'class':'WW6dff uQIVzc Sksgp'})
        news_reporting_datetime = news_reporting.get('datetime').split('T')
        news_reporting_date, news_reporting_time = news_reporting_datetime[0], news_reporting_datetime[1][:-1] 
        reporting_dates.append(news_reporting_date)
        reporting_times.append(news_reporting_time)
    result = {'link': links, 'title': titles, 'agency': agencies,\
        'date': reporting_dates, 'time': reporting_times}
    return result

#executing function
search_word = input("겁색어를 입력하세요")
news= google_news_clipping_keyword(search_word, 2)
print(news)
