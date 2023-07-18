import requests

url = 'https://overstudy.com/parathon'

r = requests.get(url)

print(r.headers)
for key in r.headers:
    print(key, ":", r.headers[key])
print('-----------')
# 딕셔너리 대소문자 구별 안함
print(r.headers.get('x-parathon-study')) # 안전상의 이유
print(r.headers.get('X-PARATHON-STUDY'))  # case-insensitive
