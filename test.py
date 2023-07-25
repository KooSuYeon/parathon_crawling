import requests

r = requests.get('https://overstudy.com/parathon')

with open('parathon.html', 'w', encoding='utf8') as file:
    file.write(r.text)