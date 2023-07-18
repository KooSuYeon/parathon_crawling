import requests

login_url = 'https://overstudy.com/parathon/api/login'

payload = {
    'username': 'admin',
    'passcode': '045'
}

r = requests.post(login_url, payload)

info_url = 'https://overstudy.com/parathon/api/getinfo'


