import requests

url = 'https://overstudy.com/parathon'

r = requests.get(url)

print(r.cookies)
print('-----------')
print(r.cookies.get('sample_cookie'))