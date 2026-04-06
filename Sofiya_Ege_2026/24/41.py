import re
t=open(r'C:\Users\Zarif\Downloads\1696_1.txt').readline()
m=re.findall(r'(?:\([1-9]\d*[^05][+-][1-9][0-9]*[05]\))+', t)
#m=re.findall(r'(?:()', t)
print(len(max(m, key=len)))
print(max(m, key=len))