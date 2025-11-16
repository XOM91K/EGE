import re
l=open(r'C:\Users\Zarif\Downloads\195_1 (9).txt').readline()
m=re.findall(r'2[KNLF]+2', l)
print(len(max(m,key=len)))