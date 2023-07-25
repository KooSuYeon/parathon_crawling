import requests
from bs4 import BeautifulSoup

r = requests.get('https://overstudy.com/parathon')

soup = BeautifulSoup(r.text, 'html.parser')

div = soup.div.div

print(div.parent.contents)

for child in div.parent.contents:
    if child.string == '\n':
        _ = child.extract()  # pops out element; for strings and tags.
        # .decompose() -> delete element and get rid out of memory; for only tags.

print('------------')
print('name:', div.parent.name)
print('sibling:', div.next_sibling)
