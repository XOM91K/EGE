import re
s = open(r'C:\Users\Zarif\Downloads\988_1 (3).txt').readline()
m = re.findall(r'(?:\.\w*){6}\.', s)
print(len(min(m,key=len)))