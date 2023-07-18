import time
import requests

start = time.time()

url = 'https://overstudy.com/parathon/long_response'  # takes >5 seconds to respond

r = requests.get(url) # no limit, it waits forever

duration = round(time.time() - start, 2)  # elapsed time

print(r.text, f'(took {duration}secs)')

print('----------')

#r_timeout = requests.get(url, timeout=5) # erroneous script (comment this line)

try:
    response = requests.get(url, timeout=5)
except requests.exceptions.Timeout:
    print('Request timed out!')
