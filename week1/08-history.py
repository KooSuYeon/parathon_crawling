import requests

url = 'https://overstudy.com/parathon/deprecated' #오래되어서 쓰지 않는..

r1 = requests.get(url)

print('r1.url =', r1.url)  # final destination -> re
print('r1.status_code =', r1.status_code)  # final status code
print('r1.history =', r1.history)  # show history (redirect된 기록)
print('---------')

r2 = requests.get(url, allow_redirects=False)  # disallow redirects

print('r2.url =', r2.url)
print('r2.status_code =', r2.status_code)
print('r2.history =', r2.history)
print('---------')

print(r1.history[1].status_code)  # access each redirections by list slicing
