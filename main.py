__author__ = 'johnson'

import login
import courses
import courseOperation
import xmlHelper

profileSrc = 'xml/profile.xml'

myXmlHelper = xmlHelper.XmlHelper(profileSrc)

studentID = myXmlHelper.get_value('studentID')
password = myXmlHelper.get_value('password')
courseCode = myXmlHelper.get_value('courseCode')

myLogin = login.Login(studentID, password)
myLogin.init()
urlOpener = myLogin.get_urlopener()
loginCookie = myLogin.get_login_cookie()

myCourse = courses.Courses(urlOpener)
myCourse.get_course_data()

myCourseOperation = courseOperation.CourseOperation(urlOpener)
myCourseOperation.get_course_panel()
myCourseOperation.add_course(courseCode)