import re
s = open(r'C:\Users\Zarif\Downloads\1125_1 (2).txt').readline()
m = re.findall(r'[a-z]*@[a-z]*\.[a-z]*', s)
print(max(m, key=len))
print(len(max(m, key=len)))