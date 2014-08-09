__author__ = 'johnson'


class Courses:
    courseTableUrl = 'http://xk.fudan.edu.cn/xk/courseTableServlet'
    courseHtmlSrc = 'html/courses.html'
    courseData = ''

    def __init__(self, url_opener):
        self.url_opener = url_opener

    def get_course_data(self):
        self.courseData = self.url_opener.open(self.courseTableUrl).read()
        course_html_file = open(self.courseHtmlSrc, 'wb')
        course_html_file.write(self.courseData)
        course_html_file.close()
        print 'store course file to ' + self.courseHtmlSrc