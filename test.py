__author__ = 'johnson'

import re

myFile = open('coursePanel.html', 'r')
myStr = myFile.read()

p = 123
print('%d', p)

pattern = re.compile('[\s\S]*(\d+)[\s\S]*')
match = pattern.match(myStr)
if match:
    print match.group(1)
