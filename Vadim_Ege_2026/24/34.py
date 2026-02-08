import re
l = open(r'C:\Users\Zarif\Downloads\1265_1 (5).txt').readline()
m = re.findall(r'(?:(?:[789][0-9]*|0)[-*])+(?:[789][0-9]*|0)',l)
print(max(m, key=len))
print(len(max(m,key=len)))