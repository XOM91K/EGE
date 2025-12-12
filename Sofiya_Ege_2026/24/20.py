import re
t=open(r'C:\Users\Zarif\Downloads\24 (28).txt').readline()
m=re.findall(r'F?(?:EF)+E?', t)
print(len(max(m, key=len)))
