import re
s = open('/Users/zarif/Downloads/988_1.txt').readline()
m = re.findall(r'(?:\.\w*){6}\.',s)
print(len(min(m,key=len)))