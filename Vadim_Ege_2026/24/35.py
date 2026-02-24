import re
l = open(r'C:\Users\Zarif\Downloads\1565_1 (6).txt').readline()
m = re.findall(r'(?:BAC|CAB){24}',l)
print(max(m,key=len))
print(len(max(m,key=len)))
print(len(max(m,key=len)) // 3)