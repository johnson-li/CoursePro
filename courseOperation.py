__author__ = 'johnson'

import re
import urllib
import urllib2
import Image


class CourseOperation:
    __coursePanelUrl = 'http://xk.fudan.edu.cn/xk/input.jsp'
    __coursePanelSrc = 'html/coursePanel.html'
    __courseVerificationImageSrc = 'image/courseVerificationImage.jpg'
    __addCoursePostUrl = 'http://xk.fudan.edu.cn/xk/doSelectServlet'
    __dropCoursePostUrl = 'http://xk.fudan.edu.cn/xk/doUnselectServlet'
    __responseHtmlSrc = 'html/addCourseResponse.html'
    __coursePanelData = ''

    def __init__(self, url_opener):
        self.urlOpener = url_opener

    def get_course_panel(self):
        self.__coursePanelData = self.urlOpener.open(self.__coursePanelUrl).read()
        course_panel_file = open(self.__coursePanelSrc, 'wb')
        course_panel_file.write(self.__coursePanelData)
        course_panel_file.close()
        print 'course panel html file stored to ' + self.__coursePanelSrc

    def get_token(self):
        pattern = re.compile('[\s\S]*image\.do\?token=(\d+)[\s\S]*')
        match = pattern.match(self.__coursePanelData)
        if match:
            return match.group(1)
        print 'token not found error'

    def store_verification_image(self):
        image_url = 'http://xk.fudan.edu.cn/xk/image.do?token=' + str(self.get_token())
        image_data = self.urlOpener.open(image_url).read()
        image_file = open(self.__courseVerificationImageSrc, 'wb')
        image_file.write(image_data)
        image_file.close()
        print 'store image to ' + self.__courseVerificationImageSrc

    def __add_course_post(self, course_code, verification_code):
        headers = {'User-Agent': '"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0"',
                   'Referer': 'http://xk.fudan.edu.cn/xk/input.jsp', 'Connection': 'keep-alive',
                   'Host': "xk.fudan.edu.cn", 'Accept-Language': 'en-US,en;q=0.5',
                   'Accept-Encoding': 'gzip, deflate', 'Host': 'xk.fudan.edu.cn',
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
        post_data = {'token': self.get_token(), 'selectionId': course_code,
                     'xklb': 'ss', 'rand': verification_code}
        print post_data
        post_data = urllib.urlencode(post_data)
        request = urllib2.Request(self.__addCoursePostUrl, post_data, headers)
        response = self.urlOpener.open(request)
        response_data = response.read()
        response_html_file = open(self.__responseHtmlSrc, 'wb')
        response_html_file.write(response_data)
        response_html_file.close()

    def add_course(self, course_code):
        self.store_verification_image()
        print 'please input verification code'
        image = Image.open(self.__courseVerificationImageSrc)
        image.show()
        verification_code = raw_input()

        self.__add_course_post(course_code, verification_code)

    def __drop_course_post(self, course_code, verification_code):
        headers = {'User-Agent': '"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0"',
                   'Referer': 'http://xk.fudan.edu.cn/xk/input.jsp', 'Connection': 'keep-alive',
                   'Host': "xk.fudan.edu.cn", 'Accept-Language': 'en-US,en;q=0.5',
                   'Accept-Encoding': 'gzip, deflate',
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
        post_data = {'token': self.get_token(), 'selectionId': course_code,
                     'xklb': '', 'rand': verification_code}
        print post_data
        post_data = urllib.urlencode(post_data)
        request = urllib2.Request(self.__dropCoursePostUrl, post_data, headers)
        response = self.urlOpener.open(request)
        response_data = response.read()
        response_html_file = open(self.__responseHtmlSrc, 'wb')
        response_html_file.write(response_data)
        response_html_file.close()

    def drop_course(self, course_code):
        self.store_verification_image()
        print 'please input verification code'
        verification_code = raw_input()
        self.__drop_course_post(course_code, verification_code)