from PIL import Image
import requests as rq

import URL
import panel
from common import save_to_file


class Login(object):

    RESULT_FILE = 'html/loginResult.html'
    IMAGE_FILE = 'image/loginVerificationCode.jpg'
    USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0'

    def __init__(self, student_id, password):
        self.student_id = student_id
        self.password = password
        self.__session = rq.Session()
        self.__session.headers['User-Agent'] = self.USER_AGENT

    def login(self):
        self.__session.get(URL.SITE)
        img = self.__session.get(URL.LOGIN_IMAGE)
        save_to_file(img.content, self.IMAGE_FILE,
                     'please input verification code manually')
        Image.open(self.IMAGE_FILE).show()
        verification_code = raw_input()
        if self._do_login(verification_code):
            print 'login successful'
        else:
            raise Exception('login failed')
        return panel.Panel(self.__session)

    def _do_login(self, verification_code):
        #headers = {'Referer': URL.SITE}
        post_data = {'studentId': self.student_id, 'password': self.password,
                     'Submit2': 'Submit', 'rand': verification_code}
        page = self.__session.post(URL.LOGIN, data=post_data)
        save_to_file(page.content, self.RESULT_FILE)
        return len(page.content) < 2000
