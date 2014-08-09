__author__ = 'johnson'

import urllib2
import urllib
import cookielib

host = 'xk.fudan.edu.cn'
hostUrl = 'http://xk.fudan.edu.cn/xk/'
courseTableUrl = 'http://xk.fudan.edu.cn/xk/courseTableServlet'
inputTabUrl = 'http://xk.fudan.edu.cn/xk/input.jsp'
postUrl = 'http://xk.fudan.edu.cn/xk/loginServlet'
imageUrl = "http://xk.fudan.edu.cn/xk/image.do"
htmlFileSrc = 'index.html'
courseFileSrc = 'course.html'
inputFileSrc = 'input.jsp'
imageFileSrc = 'image.jpg'

cookie = cookielib.LWPCookieJar()
cookieSupport = urllib2.HTTPCookieProcessor(cookie)
urlOpener = urllib2.build_opener(cookieSupport)
urlOpener.open(hostUrl)
print cookie

response = urllib2.urlopen(hostUrl)

imageData = urlOpener.open(imageUrl).read()
imageFile = open(imageFileSrc, 'wb')
imageFile.write(imageData)
imageFile.close()

print 'image file sore to ' + imageFile.name
rand = raw_input()

headers = {'User-Agent': '"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0"',
           'Refer': 'http://xk.fudan.edu.cn/xk/'}
postData = {'studentId': '12307130211', 'password': '093418', 'Submit2': 'Submit', 'rand': rand}
postData = urllib.urlencode(postData)

request = urllib2.Request(postUrl, postData, headers)
loginResponse = urlOpener.open(request)
loginPage = loginResponse.read()

htmlFile = open(htmlFileSrc, 'wb')
htmlFile.write(loginPage)
htmlFile.close()

courseTable = urlOpener.open(courseTableUrl).read()
courseFile = open(courseFileSrc, 'wb')
courseFile.write(courseTable)
courseFile.close()

inputTab = urlOpener.open(inputTabUrl).read()
inputTabFile = open(inputFileSrc, 'wb')
inputTabFile.write(inputTab)
inputTabFile.close()

postData = {'selectionId': 'FINE110001.01',
            'token': '5437',
            'xklb': 'ss',
            'rand': 'fnmd'}
