__author__ = 'johnson'

import login
#import courses
#import courseOperation
#import xmlHelper
import config

# TODO check config
# [PEP8] variables and functions: lowercase separated by underscores
student_id = config.STUDENT_ID
password = config.PASSWORD
course_code = config.COURSE_CODE



#myCourse = courses.Courses(urlOpener)
#myCourse.get_course_data()

#myCourseOperation = courseOperation.CourseOperation(urlOpener)
#myCourseOperation.get_course_panel()
#myCourseOperation.add_course(courseCode)

def main():
    my_login = login.Login(student_id, password)
    try:
        my_login.login()
        opener = my_login.get_urlopener()
    except Exception as ex:
        print ex.args[0]

if __name__ == '__main__':
    main()
