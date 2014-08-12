import login
import config

# TODO check config
# [PEP8] variables and functions: lowercase separated by underscores
student_id = config.STUDENT_ID
password = config.PASSWORD
course_code = config.COURSE_CODE

def main():
    my_login = login.Login(student_id, password)
    try:
        panel = my_login.login()
        panel.get_course_table()
        panel.get_course_panel()
        #panel.add_course(course_code)
        panel.drop_course(course_code)
    except Exception as ex:
        print ex.args[0]

if __name__ == '__main__':
    main()
