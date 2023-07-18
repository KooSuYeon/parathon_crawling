import requests

url1 = 'https://overstudy.com/parathon/restricted'
url2 = 'https://overstudy.com/parathon/invalid'
url3 = 'https://overstudy.com/parathon/internal_error'
url4 = 'https://overstudy.com/parathon'

r1 = requests.get(url1)
r2 = requests.get(url2)
r3 = requests.get(url3)
r4 = requests.get(url4)

# when response object is called as 'str' (magic method): returns status code
print('r1:', r1)
print('r2:', r2)
print('r3:', r3)
print('r4:', r4)

# How to check the response is ok?
if r1.status_code == requests.codes.ok: # 200번, 300번대만
    print('r1 is ok.')
else:
    print('r1 is not ok.')

if r4.status_code == requests.codes.ok:
    print('r4 is ok.')
else:
    print('r4 is not ok.')

print('----------')
# Raise exception when response is not ok
r1.raise_for_status()
# 400, 500번대
