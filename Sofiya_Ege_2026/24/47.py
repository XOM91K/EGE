import re
t=open(r'C:\Users\Zarif\Downloads\1731_1.txt').readline()
t=t.replace('02', '#')
m=re.findall(r'(?:[^#AEOIUY]*#){20}[^#AEOIUY]*[AEOIUY]', t)
print(len(max(m, key=len))+20 + 1)
print(max(m, key=len))