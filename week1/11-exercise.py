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

// X
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
*address1: string (대한민국의 시.군.구, 예를 들어 '동작구', '마포구', '서초구' 등)

<응답 데이터 형식>
{
    code: 응답 코드 (0: 성공 / 1 ~ 3: 실패)
    msg: 응답 메시지
    data: 성공일 경우 요청된 쿼리에 맞는 데이터를 json 형태로 반환
}

'''