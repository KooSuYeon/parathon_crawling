import requests

url = 'https://overstudy.com/parathon'

r = requests.get(url)

#브라우저의 저장공간
#추적하는 용도
print(r.cookies)
print('-----------')
print(r.cookies.get('sample_cookie'))

#딕셔너리와 비슷한듯 다름 덮어씌움
#for 아래에서 유효하다.