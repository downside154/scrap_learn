# Google News Crawling
from typing import Text
from bs4 import BeautifulSoup
import requests

#/search? is disallowed by www.google.com
# will use /? instead 

# Google News Search (Search: 파이썬 = %ED%8C%8C%EC%9D%B4%EC%8D%AC)

base_url = 'https://news.google.com'
search_url = base_url + "/?q=%ED%8C%8C%EC%9D%B4%EC%8D%AC&hl=ko&gl=KR&ceid=KR%3Ako"
resp = requests.get(search_url)
html_src = resp.text
soup = BeautifulSoup(html_src, 'html.parser')

# Select News Block
news_items = soup.select('div[class="xrnccd"]')
print("length of news items : ", len(news_items))
# print("first news item : ", news_items[0])
print("\n")

# get link, title, context, agency, time published fo reach news item
# by data parsing BeautifulSoup

for item in news_items[:3]:
    link = item.find('a', attrs={'class':'VDXfz'}).get('href').split(".")[1]
    news_link = base_url + link
    print("news link : ", news_link)
    
    news_title = item.find('a', attrs={'class':'DY5T1d'}).getText()
    print("news title : ", news_title)

    #this code is depreciated in google news
    # news_content = item.find('span', attrs={'class':'xBbh9'}).text
    # print("news content : ", news_content)

    news_agency = item.find('a', attrs={'class':'wEwyrc AVN2gc uQIVzc Sksgp'}).text
    print("news agency : ", news_agency)

    news_reporting = item.find('time', attrs={'class':'WW6dff uQIVzc Sksgp'})
    news_reporting_datetime = news_reporting.get('datetime').split('T')
    news_reporting_date, news_reporting_time = news_reporting_datetime[0], news_reporting_datetime[1][:-1] 
    print(f"Date: {news_reporting_date}   Time : {news_reporting_time}")
    print("\n")



#Combining all into a news clipping
def google_news_clipping(url, limit=5):

    resp = requests.get(url)
    html_src=resp.text
    soup = BeautifulSoup(html_src, 'html.parser')

    news_item = soup.select('div[class="xrnccd"]')

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
news = google_news_clipping(search_url, 4)
print(news)