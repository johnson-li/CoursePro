""" Don't repeat yourself, put constants in one place.
"""

#hostUrl = 'http://xk.fudan.edu.cn/xk/'
#postUrl = 'http://xk.fudan.edu.cn/xk/loginServlet'
#loginImageUrl = "http://xk.fudan.edu.cn/xk/image.do"
SITE = 'http://xk.fudan.edu.cn/xk/'
SITE_ENG = SITE + 'languageServlet?languager=isEn'
LOGIN = SITE + 'loginServlet'
LOGIN_IMAGE = SITE + 'image.do'
COURSE_TABLE = SITE + 'courseTableServlet'
COURSE_PANEL = SITE + 'input.jsp'
COURSE_PANEL_IMAGE = LOGIN_IMAGE + '?token='
COURSE_ADD = 'http://xk.fudan.edu.cn/xk/doSelectServlet'
COURSE_DROP = 'http://xk.fudan.edu.cn/xk/doUnselectServlet'
