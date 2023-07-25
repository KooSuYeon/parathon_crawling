import requests
from bs4 import BeautifulSoup

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'

r = requests.get(
    url='https://www.acmicpc.net/problem/17404',
    headers={'User-Agent': USER_AGENT}
)

soup = BeautifulSoup(r.text, 'html.parser')

# 1. 문제 제목을 str 형태로 저장
problem_title: str = soup.select_one('#problem_title').text

# 2. 예제 입력 1을 str 형태로 저장
sample_input_1: str = '여기에 코드를 작성해주세요.'

# 3. 문제를 만든 사람을 str 형태로 저장
created_by: str = '여기에 코드를 작성해주세요.'

# 4. 문제의 정답 비율을 float 형태로 저장 ('%' 기호 제외)
rate: float = '여기에 코드를 작성해주세요.'

# 5. 문제 본문 전체를 str 형태로 저장
problem_body: str = '여기에 코드를 작성해주세요.'



# 여기부터는 채점 및 결과 확인 코드입니다.
print('문제 제목:', problem_title, end='\n--------\n')
print('예제 입력 1:', sample_input_1, end='\n--------\n')
print('문제를 만든 사람:', created_by, end='\n--------\n')
print('정답 비율: %.3f%%' % rate, end='\n--------\n')
print('문제:', problem_body, end='\n--------\n')

values = [problem_title, sample_input_1, created_by, rate, problem_body]
ANSWER = [
    'RGB거리 2',
    '3 26 40 83 49 60 57 13 89 99',
    'baekjoon',
    58.498,
    'RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집 이 순서대로 있다.\n'
    '집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 각각의 집을 빨강, 초록,  파랑으로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을 칠하는  비용의 최솟값을 구해보자.'
]


def judge(user_input, answer) -> int:
    for idx, (a, b) in enumerate(zip(user_input, answer), start=1):
        if isinstance(b, float) and a == b: continue
        if ''.join(a.split()) != ''.join(b.split()):
            return idx
    return 0


result = judge(values, ANSWER)
if result == 0:
    print('정답입니다!')
else:
    print(f'{result}번 문제 오답입니다.')
