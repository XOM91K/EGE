#‪C:\Users\Zarif\Downloads\24 (30).txt
import re
t=open(r'C:\Users\Zarif\Downloads\24 (30).txt').readline()
t=t.replace('20', '#')
m=re.findall(r'(?=((?:#[^#AEIOUY]*){26}[AEIOUY]))',t)
print(len(min(m, key=len)) + 26)
print((min(m, key=len)))