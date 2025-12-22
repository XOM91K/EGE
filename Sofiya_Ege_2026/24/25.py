import re
a=open(r'C:\Users\Zarif\Downloads\1565_1 (1).txt').readline()
m=re.findall(r'(?:BAC|CAB){24}', a)
print(len(max(m, key=len)))
