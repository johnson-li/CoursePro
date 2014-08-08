__author__ = 'johnson'

import urllib2
import urllib
import cookielib

hostUrl = 'http://xk.fudan.edu.cn/xk/'
postUrl = 'http://xk.fudan.edu.cn/xk/loginServlet'
imageUrl = "http://xk.fudan.edu.cn/xk/image.do"
htmlFileSrc = 'index.html'
imageFileSrc = 'image.jpg'

cj = cookielib.LWPCookieJar()
cookieSupport = urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(cookieSupport, urllib2.HTTPHandler)
urllib2.install_opener(opener)

response = urllib2.urlopen(hostUrl)

imageData = urllib.urlopen(imageUrl).read()
imageFile = open(imageFileSrc, 'wb')
imageFile.write(imageData)
imageFile.close()

rand = raw_input()

headers = {'User-Agent': '"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0"'}
postData = {'studentId': '12307130211', 'password': '093418', 'Submit2': 'Submit', 'rand': rand}
postData = urllib.urlencode(postData)

request = urllib2.Request(postUrl, postData, headers)
loginResponse = urllib2.urlopen(request)
loginPage = loginResponse.read()

htmlFile = open(htmlFileSrc, 'wb')
htmlFile.write(loginPage)
htmlFile.close()