import requests

url = 'https://overstudy.com/parathon'

r = requests.get(url)

for i in r.headers:
    print(i,":", r.headers[i])

print(r.headers.get("X-Parathon-Study"))




