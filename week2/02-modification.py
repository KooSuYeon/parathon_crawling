import requests
from bs4 import BeautifulSoup

r = requests.get('https://overstudy.com/parathon')

soup = BeautifulSoup(r.text, 'html.parser')

soup.title.string = 'CHANGED_TITLE'
soup.title.name = 'changed_name'

print(soup)

print('title:', soup.title)
print('changed_name:', soup.changed_name)
