'''
Login
method: POST
URL: https://overstudy.com/parathon/api/login
request: form data
response: json

<요청 데이터 형식>
username: admin
passcode: leading zero를 포함한 000 ~ 100 사이 3자리 정수 (30이면 '030'으로)

<응답 데이터 형식>
{
    code: 응답 코드 (0: 성공 / 1 ~ 3: 실패)
    msg: 응답 메시지
}
'''

import requests

url = 'https://overstudy.com/parathon/api/login'

password = 0
for i in range(100):

    payload = {
        'username' : 'admin',
        'passcode' : str(i).zfill(3),
    }
    r = requests.post(url, data = payload)
    datum = r.json()
    print(f"inputting {i} ...", end = '\r')

    if datum.get('code') == 0: 
        password = i
        break

print('username : admin\n' + 'passcode : ' + str(password))

'''

Logout
method: GET
URL: https://overstudy.com/parathon/api/logout
request: null
response: json


Getinfo
method: GET
URL: https://overstudy.com/parathon/api/getinfo
request: url query parameters
response: json

** 헤더의 X-Auth-Token 을 'parathon'으로 설정해야 함! **
** 로그인 되어 있어야 함! **

<요청 데이터 형식> (*표시된 항목은 필수 항목)
*category: string (건설업, 도매업, 소매업, 숙박업, 음식업, 제조업 등)
*address1: string (대한민국의 시.도, 예를 들어 '서울특별시', '세종특별자치시', '전라남도' 등)
*address2: string (대한민국의 시.군.구, 예를 들어 '동작구', '마포구', '서초구' 등)

<응답 데이터 형식>
{
    code: 응답 코드 (0: 성공 / 1 ~ 3: 실패)
    msg: 응답 메시지
    data: 성공일 경우 요청된 쿼리에 맞는 데이터를 json 형태로 반환
}
'''

import requests


class Exercise:

    url = 'https://overstudy.com/parathon/api'

    def __init__(self):
        self.session = requests.Session()

        self.session.headers.update({'X-Auth-Token': 'parathon'})
        self.logged_in = False

    def login(self, received: int):

        payload = {
            'username' : 'admin',
            'passcode' : str(received).zfill(3),
        }
        login_info = self.session.post(self.url+ '/login', data = payload)
        datum = login_info.json().get('code')
        if datum == 0:
            self.logged_in = True
            return True
        else:
            return False

    def getinfo(self, category: str, address1 : str = '', address : str = ''):
        if self.logged_in == False:
            print("로그인 먼저 하세요")
            return
        param = {
            'category' : category,
            'address1' : address1,
            'address2' : address2,
        }

        num_info = self.session.get(self.url + '/getinfo', params = param)

        datum = num_info.json()
        print("code :", datum.get('code'))
        print("msg :",datum.get('msg'))
        txt = datum.get('data')
        for i in txt:
            print(i)

    def close(self):
        self.session.close()


if __name__ == '__main__':
    print("로그인을 진행합니다.")

    ec = Exercise()
    for i in range(101):
        print(f"inputting '{i}'....", end = "\r")

        if(ec.login(i)):
            print("로그인 성공!            ")
            break
    else:
        print("로그인 못함;;")
        exit(1)
    

    while(True):
        category = input("카테고리를 입력하세요 >> ")
        if category == 'end':
            break
        address1 = input("도시를 입력하세요 >> ")
        address2 = input("지역구를 입력하세요 >> ")

        ec.getinfo(category, address1, address2) 
        retry = input("다시 검색하시겠습니까? (y/n) >> ")
        if retry == 'y':
            continue
        else:
            break

    ec.close()