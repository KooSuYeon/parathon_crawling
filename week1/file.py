import requests

s = requests.Session()
s.headers.update({"X-Auth-Token": 'parathon'})
url = 'https://overstudy.com/parathon/api/login'

payload = {'username' : 'admin', 'passcode' : str(45).zfill(3)}

r = s.post(url, payload)

info_url = 'https://overstudy.com/parathon/api/getinfo'

param = {"category": "건설업", "address1": "서울특별시", "address2": }
r2 = s.get(info_url, params=param)

response = r.json()
print(response)
print(r2.json())
    

# for i in range(0,100):
#     payload = {'username' : 'admin', 'passcode' : str(45).zfill(3)}

# if response['code'] == 0:
#         pass 
#     print(i, response)

