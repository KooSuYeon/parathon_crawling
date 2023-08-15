import time
import pandas as pd
import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'

years = list(range(2010,2019))
months = list(range(1,13))
weeks = list(range(0,5))

rating_pages = []

url = 'https://workey.codeit.kr/ratings/index'
namuwiki_url = 'https://namu.wiki/w/'

print("나무위키에 접속하세요")

# 방송 시간 찾는 함수
def findTime(program):
    if '(' in program:
        for i in range(len(program)):
            if program[i] == '(':
                program = program[i+1:-1]
                break
    try:
        time.sleep(1)
        r2 = requests.get(namuwiki_url+program, headers={'User-Agent': USER_AGENT})
    except:
        findTime(program)
        pass

    while r2.status_code == "429":
        print("홈페이지를 새로고침 해주세요")
        time.sleep(5)
        findPeriod(program)

    #상태 코드 확인 
    print(r2.status_code)
    if r2.status_code != requests.codes.ok:
        return None
    soup2 = BeautifulSoup(r2.text, 'html.parser')
    if soup2.select("div.wiki-table-wrap.table-right"):
        high = soup2.select("div.wiki-table-wrap.table-right")
        for sibling in high:
            for item in sibling.select('tr'):
                for div_class in item.select('td > div'):
                    if div_class.select('strong'):
                        if div_class.select("strong")[0].text == "방송 시간":
                            return div_class.parent.nextSibling.div.text
                    else:
                        if div_class.text == "방송 시간":
                            return div_class.parent.nextSibling.div.text
# 방송 기간 찾는 함수
def findPeriod(program):
    if '(' in program:
        for i in range(len(program)):
            if program[i] == '(':
                program = program[i+1:-1]
                break
    
    try:
        time.sleep(1)
        r2 = requests.get(namuwiki_url+program, headers={'User-Agent': USER_AGENT})
    except:
        findPeriod(program)
        pass

    while r2.status_code == "429":
        print("홈페이지를 새로고침 해주세요")
        time.sleep(5)
        findPeriod(program)

    if r2.status_code != requests.codes.ok:
        return None
    soup2 = BeautifulSoup(r2.text, 'html.parser')
    if soup2.select("div.wiki-table-wrap.table-right"):
        high = soup2.select("div.wiki-table-wrap.table-right")
        for sibling in high:
            for item in sibling.select('tr'):
                for div_class in item.select('td > div'):
                    if div_class.select('strong'):
                        if div_class.select("strong")[0].text == "방송 기간":
                            return div_class.parent.nextSibling.div.text
                            
                    else:
                        if div_class.text == "방송 기간":
                            return div_class.parent.nextSibling.div.text

# payload = {'year': '2011', 'month': '2', 'week': '1'}

# r = requests.get(url, payload)
# soup = BeautifulSoup(r.text,'html.parser')
# rating_pages.append(soup)

for year in years:
    for month in months:
        for week in weeks:
            payload = {'year': year, 'month': month, 'week': week}
            r = requests.get(url, payload)
            soup = BeautifulSoup(r.text,'html.parser')

            if len(soup.select('.row')) > 1:
                rating_pages.append(soup)

records = []

for page in rating_pages:
    date = page.select('option[selected=selected]')[2].text
    ranks = page.select('.row .rank')[1:]
    channels = page.select('.row .channel')[1:]
    programs = page.select('.row .program')[1:]
    

    for i in range(10):
        record = []
        record.append(date)
        record.append(ranks[i].text)
        record.append(channels[i].text)
        record.append(programs[i].text)
        record.append(findTime(programs[i].text))
        record.append(findPeriod(programs[i].text))
        records.append(record)

df = pd.DataFrame(data=records, columns=['date', 'rank', 'channel', 'program', 'time', 'Namuperiod'])

#형식없는 표 형태
print(df)

#표 형태
df