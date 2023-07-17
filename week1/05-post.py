import requests

url = 'https://overstudy.com/parathon/test/login'

payload = {}

payload['user'] = input('Input username >>> ').rstrip()
payload['pass'] = input('Input passcode >>> ').rstrip()

r = requests.post(url, data=payload)

print('Response:', r.text)
