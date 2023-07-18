import requests

url = 'https://overstudy.com/parathon/test/login'

payload = {}

payload['user'] = input('Input username >>> ').rstrip()
payload['pass'] = input('Input passcode >>> ').rstrip()

#로그인할때, 검색할때, 클라이언트가 서버에 요청할 때
#form data -> post 딕셔너리 자체를 보낸다. 
r = requests.post(url, data=payload) # text 자체

print('Response:', r.text) 
