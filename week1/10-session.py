import requests

#cookie를 통해서 구현

url = 'https://overstudy.com/parathon'

r1 = requests.get(url)
r2 = requests.get(url) # 다른 환경으로 인식

print('(r1) session =', r1.cookies.get("SESSION"))
print('(r2) session =', r2.cookies.get("SESSION"))
print('-------------')

s = requests.Session() #같은 환경 유지
# how to set default headers when creating session
# s.headers.update({'X-Test-Header': 'test'}) -> 식별하는 용도 (공통적으로 적용)

r3 = s.get(url)
r4 = s.get(url) 

print('(r3) session =', s.cookies.get("SESSION"))
print('(r4) session =', s.cookies.get("SESSION"))

s.cookies.set('SESSION', '1234567890', domain='overstudy.com')  # override

r5 = s.get(url)

print('(r5) session =', s.cookies.get("SESSION"))
