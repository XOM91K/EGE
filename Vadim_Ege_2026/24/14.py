import re
r = open(r"C:\Users\Zarif\Downloads\827_1 (4).txt").readline()
m = re.findall(r'B(?:\d+[-*])+\d+',r)
print(max(m,key=len))
print(len(max(m,key=len)))