# import requests
# from bs4 import BeautifulSoup

# r = requests.get('https://overstudy.com/parathon')

# soup = BeautifulSoup(r.text, 'html.parser')

# print('soup.title')
# # the first matched tag
# print('tag:  ', soup.title)

# # name (tag name)
# print('name: ', soup.title.name)

# # attrubutes
# print('attrs:', soup.title.attrs)

# print('---------')
# print('soup.div.div.div')
# print('tag:  ', soup.div.div.div)
# print('name: ', soup.div.div.div.name)
# print('attrs:', soup.div.div.div.attrs)

import requests
from bs4 import BeautifulSoup

r = requests.get('https://overstudy.com/parathon')

soup = BeautifulSoup(r.text, 'html.parser')

soup.title.string = "Parathon"
soup.title.name = 'title'
print('soup.title')

print('tag: ', soup.title)
print('name: ', soup.title.name)
print('attributes : ', soup.title.attrs)

print("---------------")
print('soup.div.div.div')
print('tag: ', soup.div.div.div)
print('name: ', soup.div.div.div.name)
print('attrs: ', soup.div.div.div.attrs)
