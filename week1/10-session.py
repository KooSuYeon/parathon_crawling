import requests

url = 'https://overstudy.com/parathon'

r1 = requests.get(url)
r2 = requests.get(url)

print('(r1) session =', r1.cookies.get("SESSION"))
print('(r2) session =', r2.cookies.get("SESSION"))
print('-------------')

s = requests.Session()
# how to set default headers when creating session
# s.headers.update({'X-Test-Header': 'test'})

r3 = s.get(url)
r4 = s.get(url)

print('(r3) session =', s.cookies.get("SESSION"))
print('(r4) session =', s.cookies.get("SESSION"))

s.cookies.set('SESSION', '1234567890', domain='overstudy.com')  # override

r5 = s.get(url)

print('(r5) session =', s.cookies.get("SESSION"))
