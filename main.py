__author__ = 'johnson'

import login
import courses
import courseOperation

studentID = '12307130211'
password = ''
courseCode = 'FINE110001.01'

myLogin = login.Login(studentID, password)
myLogin.init()
urlOpener = myLogin.get_urlopener()
loginCookie = myLogin.get_login_cookie()

myCourse = courses.Courses(urlOpener)
myCourse.get_course_data()

myCourseOperation = courseOperation.CourseOperation(urlOpener)
myCourseOperation.get_course_panel()
myCourseOperation.add_course(courseCode)