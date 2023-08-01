import requests
from bs4 import BeautifulSoup

with open('parathon.html') as fp:
    soup = BeautifulSoup(fp, 'html.parser')

# soup.title.string = "Parathon"
# soup.title.name = 'title'

print('tag: ', soup.title)
soup.title.name = "CHANGED"
print('past tag: ', soup.title)
print('changed tag name : ', soup.CHANGED)

soup.CHANGED.string = "Changed"
print('changed tag\'s string : ' , soup.CHANGED)
print('only view tag\'s string : ', soup.CHANGED.string)
#print('attributes : ', soup.title.attrs)


print("---------------")
# print('soup.div.div.div')
print('tag: ', soup.div.div.div)
print('name: ', soup.div.div.div.name)
print('attrs: ', soup.div.div.div.attrs)
