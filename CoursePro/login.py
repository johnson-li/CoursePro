import os
import cookielib
import urllib
import urllib2
from PIL import Image


class Login:
    host = 'xk.fudan.edu.cn'
    hostUrl = 'http://xk.fudan.edu.cn/xk/'
    postUrl = 'http://xk.fudan.edu.cn/xk/loginServlet'
    loginImageUrl = "http://xk.fudan.edu.cn/xk/image.do"
    loginResultFileSrc = 'html/loginResult.html'
    VERIFICATION_IMAGE_SRC = 'image/loginVerificationCode.jpg'

    #student id and password is initiated to init this class
    #init cookie handler and login
    def __init__(self, student_id, password):
        self.student_id = student_id
        self.password = password

        self.__url_opener = urllib2.build_opener()
        self.__cookie_jar = cookielib.LWPCookieJar()

        cookie_support = urllib2.HTTPCookieProcessor(self.__cookie_jar)
        self.__url_opener = urllib2.build_opener(cookie_support)
        self.__url_opener.open(self.hostUrl)

    def login(self):
        self.store_image(self.__url_opener)
        print 'please input verification code manually'
        image = Image.open(self.VERIFICATION_IMAGE_SRC)
        image.show()
        verification_code = raw_input()

        if self.do_login(verification_code):
            print 'login successful'
        else:
            raise Exception('login failed')

    def do_login(self, verification_code):
        """ login with verification code
        """
        headers = {'User-Agent': '"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0"',
                   'Referer': 'http://xk.fudan.edu.cn/xk/'}
        post_data = {'studentId': self.student_id, 'password': self.password,
                     'Submit2': 'Submit', 'rand': verification_code}
        post_data = urllib.urlencode(post_data)
        request = urllib2.Request(self.postUrl, post_data, headers)
        login_response = self.__url_opener.open(request)
        login_page = login_response.read()
        if not os.path.exists('html'):
            os.path.mkdir('html')
        self.__store_html(login_page, self.loginResultFileSrc)
        return len(login_page) < 2000

    #output response data to a html file
    @staticmethod
    def __store_html(data, html_src):
        html_file = open(html_src, 'wb')
        html_file.write(data)
        html_file.close()

    #get urlopener which contains identification cookie
    def get_urlopener(self):
        return self.__url_opener

    #store login verification code image
    def store_image(self, urlopener):
        image_data = urlopener.open(self.loginImageUrl).read()
        if not os.path.exists('image'):
            os.path.mkdir('image')
        image_file = open(self.VERIFICATION_IMAGE_SRC, 'wb')
        image_file.write(image_data)
        image_file.close()
        print 'login verification code image stored to ' + image_file.name

    #get the cookie that contains login information
    def get_login_cookie(self):
        return self.__cookie_jar
