import requests


class ExerciseCrawler:
    def __init__(self):
        # create session
        self.session = requests.Session()

        # set default header for current session
        self.session.headers.update({'X-Auth-Token': 'parathon'})
        self.logged_in = False

    def login(self, passcode: int):
        payload = {
            'username': 'admin',
            'passcode': str(passcode).zfill(3)
        }
        r = self.session.post(self._get_url('login'), data=payload)
        code = r.json().get('code')
        if code == 0:
            self.logged_in = True
            return True
        elif code == 2:
            return False
        else:
            raise RuntimeError('Login Failed!')

    def logout(self):
        self.session.post(self._get_url('logout'))
        self.logged_in = False

    def search(self, category: str, address1: str = '', address2: str = ''):
        if not self.logged_in:
            print('you must log in first!')
            return
        params = {
            'category': category,
            'address1': address1,
            'address2': address2
        }
        r = self.session.get(self._get_url('getinfo'), params=params)

        data = r.json()
        print('--- Response ---')
        print('code:', data.get('code'))
        print('msg:', data.get('msg'))
        if (data.get('code') == 0):
            for d in data.get('data'):
                print(d)
        print('----------------')
    def close(self):
        self.session.close()

    @staticmethod
    def _get_url(path: str):
        DOMAIN = 'https://overstudy.com/parathon/api/'
        return DOMAIN + path


if __name__ == '__main__':
    ec = ExerciseCrawler()

    for i in range(101):
        print(f'trying "{i}" as passcode...', end='\r')
        if (ec.login(i)):
            print('login success!            ')
            break
    else:
        print('None of the above passcodes match.')
        exit(1)

    while True:
        category = input('input category >>> ')
        if category == 'end':
            break
        address1 = input('input address1 >>> ')
        address2 = input('input address2 >>> ')
        
        ec.search(
            category=category,
            address1=address1,
            address2=address2
        )
        
    ec.close()
