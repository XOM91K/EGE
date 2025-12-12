import re
t=open(r'C:\Users\Zarif\Downloads\1089_1 (5).txt').readline()
m=re.findall(r'(?:[^Y.]*\.){5}[^Y.]*', t)
print(len(max(m, key=len)))
# AAAAAAAA.AAA.AAA.AAAA..