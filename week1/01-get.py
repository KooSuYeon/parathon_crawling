import requests

url = 'https://overstudy.com/parathon'

r = requests.get(url)

file_name = 'parathon-index.html'

with open(file_name, 'w', encoding = 'utf-8') as file:
    file.write(r.text)
