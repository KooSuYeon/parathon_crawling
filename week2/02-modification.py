import requests
from bs4 import BeautifulSoup

r = requests.get('https://music.bugs.co.kr/chart')

soup = BeautifulSoup(r.text,'html.parser')

titles = soup.select('p.title')
artists = soup.select('p.artist')
for rank in range(len(titles)): 
    print(str(rank) +  "위 : " + titles[rank].text.rstrip().split('\n')[1] + " , 가수: " + artists[rank].text.rstrip().split('\n')[1])