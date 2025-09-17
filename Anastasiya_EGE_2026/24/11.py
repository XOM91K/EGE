import re
s = open(r'C:\Users\Zarif\Downloads\988_1 (2).txt').readline()
m = re.findall('(?:\.\w*){6}\.', s)
print(min(m, key=len))
print(len(min(m, key=len)))