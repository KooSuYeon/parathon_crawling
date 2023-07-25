import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.crummy.com/software/BeautifulSoup/bs4/doc/')

soup = BeautifulSoup(r.text, 'html.parser')

# print(soup.find(id='getting-help'))  # find by name
# print(soup.find_all(class_='headerlink', href='#getting-help'))
# print(soup.find_all(attrs={'class': 'headerlink', 'href': '#getting-help'}))
# print(soup.find_all('section', id='kinds-of-objects'))

# ** CSS Selector **
# https://www.w3schools.com/cssref/css_selectors.php

# print(soup.select('code.docutils.literal.notranslate'))
# print(soup.select('#searching-the-tree > p:nth-child(3)'))