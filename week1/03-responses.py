from io import BytesIO
from PIL import Image
import requests

response = {}

url = 'https://overstudy.com/parathon/sample.'

# html (sample.html)
response['html'] = requests.get(url + 'html').text

# plain text (sample.txt)
response['text'] = requests.get(url + 'txt').text

# json (sample.json)
response['json'] = requests.get(url + 'json').text

# image (sample.png)
response['image'] = BytesIO(requests.get(url + 'png').content)  # refer .content to read bytes

print('--- HTML ---')
print(response['html'])

print('--- TEXT ---')
print(response['text'])

print('--- JSON ---')
print(response['json'])

img = Image.open(response['image']) # 이미지를 여는 방법
img.show()
