import requests
from bs4 import BeautifulSoup

with open('parathon.html') as fp:
    soup = BeautifulSoup(fp,'html.parser')

div = soup.div.div

print(div.parent.contents)

# for child in div.parent.contents:
#     if child.string == '\n':
#         _ = child.extract()  # pops out element; for strings and tags.
#         # .decompose() -> delete element and get rid out of memory; for only tags.

# print('------------')
print('name:', div.parent.name)
#같은 레벨
print('sibling:', div.next_sibling)
