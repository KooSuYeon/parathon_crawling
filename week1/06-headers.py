import requests

url = 'https://overstudy.com/parathon'

r = requests.get(url)

print(r.headers)
for key in r.headers:
    print(key, ':', r.headers[key])
    
print('-----------')
print(r.headers.get('x-parathon-study'))
print(r.headers.get('X-PARATHON-STUDY'))  # case-insensitive
