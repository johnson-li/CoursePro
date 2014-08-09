import os
import cookielib
import urllib
import urllib2

class Login:
    host = 'xk.fudan.edu.cn'
    hostUrl = 'http://xk.fudan.edu.cn/xk/'
    postUrl = 'http://xk.fudan.edu.cn/xk/loginServlet'
    loginImageUrl = "http://xk.fudan.edu.cn/xk/image.do"
    loginResultFileSrc = 'loginResult.html'
    cookieFileSrc = 'cookie'

    def check_cookie(self):
        return os.path.exists(self.cookieFileSrc)

    def generate_cookie(self):
        cookie = cookielib.LWPCookieJar()
        cookie_support = urllib2.HTTPCookieProcessor(cookie)
        url_opener = urllib2.build_opener(cookie_support)


    def get_cookie(self):
        if self.check_cookie():
            self.generate_cookie()



login = Login()
print login.check_cookie()