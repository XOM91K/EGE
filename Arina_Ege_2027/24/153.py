import re
s = open('/Users/zarif/Downloads/153_1.txt').readline()
m = re.findall(r'(?:PNO|NPO)+', s)
print(m)
#print(len(max(m, key=len)) // 3)