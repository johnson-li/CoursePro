import re
from PIL import Image

import URL
from common import save_to_file


class Panel(object):

    TABLE_FILE = 'html/courses.html'
    PANEL_FILE = 'html/coursePanel.html'
    IMAGE_FILE = 'image/courseVerificationImage.jpg'
    RESULT_FILE = 'html/addCourseResponse.html'

    def __init__(self, session):
        self.__session = session
        self.__token = ''
        self.__verification_code = ''

    # maybe we can do a refresh
    def get_course_panel(self):
        panel = self.__session.get(URL.COURSE_PANEL)
        save_to_file(panel.content, self.PANEL_FILE, 'course panel html saved')
        self.__token = self._get_token(panel.content)
        img = self.__session.get(URL.COURSE_PANEL_IMAGE + self.__token)
        save_to_file(img.content, self.IMAGE_FILE, 'image saved')
        print 'please input verification code'
        Image.open(self.IMAGE_FILE).show()
        self.__verification_code = raw_input()

    def add_course(self, course_code):
        print self._add_drop_course(course_code, 'ss', URL.COURSE_ADD)

    def drop_course(self, course_code):
        print self._add_drop_course(course_code, '', URL.COURSE_DROP)

    def _add_drop_course(self, course_code, xklb, url):
        #headers = {'Referer': 'http://xk.fudan.edu.cn/xk/input.jsp', 'Connection': 'keep-alive',}
        post_data = {'token': self.__token, 'selectionId': course_code,
                     'xklb': xklb, 'rand': self.__verification_code}
        result = self.__session.post(url, data=post_data)
        save_to_file(result.content, self.RESULT_FILE)
        return self._get_result(result.content)

    @staticmethod
    def _get_token(data):
        pattern = re.compile('[\s\S]*image\.do\?token=(\d+)[\s\S]*')
        match = pattern.match(data)
        return match.group(1) if match else ''

    @staticmethod
    def _get_result(data):
        pattern = re.compile('[\s\S]*[ \t]*alert\(\"(.+?)\"\);[\s\S]*]')
        match = pattern.match(data)
        return match.group(1) if match else ''

    #def show_courses(self):
    def get_course_table(self):
        courses = self.__session.get(URL.COURSE_TABLE)
        save_to_file(courses.content, self.TABLE_FILE, 'course table saved')

""" {{{
import re

N, M = 15, 8

table = [[None if j else 'Slot %d' % i  for j in range(M)] for i in range(N)]
table[0] = ['Day/Slot', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def foo():
    for i in range(N):
        for j in range(M):
            print table[i][j].split()[0] if table[i][j] else '', '\t',
        print
        if i:
            for j in range(M):
                print table[i][j].split()[1] if table[i][j] else '', '\t',
            print

def bar():
    FILE = 'html/courses.html'

    data = []
    with open(FILE, 'r') as f:
        for l in f:
            m = re.match('.*index\]\.[^=]*=(.*)', l)
            if m:
                data.append(m.group(1))
    for i in range(0, len(data), 4):
        day, slot, length = (int(data[i + j]) for j in range(3))
        m = re.match('[^>]*>([^<]*)<br/>[^>]*>([^<]*)', data[i + 3])
        content = m.group(1) + ' ' + m.group(2)
        for j in range(length):
            table[slot + j][day] = content



bar()
foo()
}}} """
