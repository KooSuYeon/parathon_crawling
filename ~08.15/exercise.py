import pandas as pd
import requests
from bs4 import BeautifulSoup

print("원하는 연도를 입력하세요(2010~2018)")
year = input()
print("원하는 월을 입력하세요(1~12)")
month = input()
print("원하는 주를 입력하세요(1~5)")
week = input()

payload = {'year': year, 'month': month, 'week': week}
url = 'https://workey.codeit.kr/ratings/index'


r = requests.get(url, payload)
soup = BeautifulSoup(r.text,'html.parser')

name = soup.select('td.program')

for rank in range(10):
    namuwiki_url = 'https://namu.wiki/w/'
    show = name[rank].text
    if '(' in show:
        for i in range(len(show)):
            if show[i] == '(':
                show = show[i+1:-1]
                break
    print(str(rank+1)+"위: " + show)
    namuwiki_url = namuwiki_url + show
    print(namuwiki_url)
    r2 = requests.get(namuwiki_url)
    print(r2.status_code)
    if r2.status_code != requests.codes.ok:
        continue
    soup2 = BeautifulSoup(r2.text, 'html.parser')
    if soup2.select("div.wiki-table-wrap.table-right"):
        high = soup2.select("div.wiki-table-wrap.table-right")
        flag = 0
        for sibling in high:
            for item in sibling.select('tr'):
                for div_class in item.select('td > div'):
                    if div_class.select('strong'):
                        if div_class.select("strong")[0].text == "방송 시간":
                            print(div_class.select("strong")[0].text)
                            print(div_class.parent.nextSibling.div.text)
                        elif div_class.select("strong")[0].text == "방송 기간":
                            print(div_class.select("strong")[0].text)
                            print(div_class.parent.nextSibling.div.text)
                            flag = 1
                    elif flag == 0:
                        if div_class.text == "방송 시간":
                            print(div_class.text)
                            print(div_class.parent.nextSibling.div.text)
                        elif div_class.text == "방송 기간":
                            print(div_class.text)
                            print(div_class.parent.nextSibling.div.text)
    else:
        print("옳지 않은 테이블입니다.")