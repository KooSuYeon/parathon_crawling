import requests

payload = {'key1': 'value1', 'key2': 'value2', 'test': '1234'}

url = 'https://overstudy.com/parathon/param'

r1 = requests.get(url)  # without parameters
r2 = requests.get(url, params=payload)  # with parameters

print('r1:', r1.text)
print('r2:', r2.text)

print(r2.url)