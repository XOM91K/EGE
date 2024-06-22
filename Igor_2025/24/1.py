import re
s = open('1.txt').readline()
m = re.findall('[1-2][0-5]?', s)
print(min(m, key=int))