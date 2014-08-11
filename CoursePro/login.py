import os
from PIL import Image
import requests as rq

import URL


class Login(object):

    RESULT_FILE = 'html/loginResult.html'
    IMAGE_FILE = 'image/loginVerificationCode.jpg'

    def __init__(self, student_id, password):
        self.student_id = student_id
        self.password = password
        self.__session = None

    def login(self):
        self.__session = rq.Session()
        self.__session.get(URL.SITE)
        img = self.__session.get(URL.LOGIN_IMAGE)
        if not os.path.exists(os.path.dirname(self.IMAGE_FILE)):
            os.makedirs(os.path.dirname(self.IMAGE_FILE))
        with open(self.IMAGE_FILE, 'wb') as f:
            f.write(img.content)
        print 'please input verification code manually'
        Image.open(self.IMAGE_FILE).show()
        verification_code = raw_input()
        if self._do_login(verification_code):
            print 'login successful'
        else:
            raise Exception('login failed')

    def _do_login(self, verification_code):
        headers = {'User-Agent': '"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0"',
                   'Referer': 'http://xk.fudan.edu.cn/xk/'}
        post_data = {'studentId': self.student_id, 'password': self.password,
                     'Submit2': 'Submit', 'rand': verification_code}
        page = self.__session.post(URL.LOGIN, headers=headers, data=post_data)
        if not os.path.exists(os.path.dirname(self.RESULT_FILE)):
            os.makedirs(os.path.dirname(self.RESULT_FILE))
        with open(self.RESULT_FILE, 'wb') as f:
            f.write(page.content)
        return len(page.content) < 2000

    def get_session(self):
        return self.__session
