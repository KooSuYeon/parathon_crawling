import requests

url = 'https://overstudy.com/parathon'

r = requests.get(url)

print(r.headers)
print('-----------')
print(r.headers.get('x-parathon-study'))
print(r.headers.get('X-PARATHON-STUDY'))  # case-insensitive
