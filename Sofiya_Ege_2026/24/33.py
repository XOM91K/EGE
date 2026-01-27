import re
t=open(r'C:\Users\Zarif\Downloads\24-215 (2).txt').readline()
m=re.findall(r'(?:[ABC][123][ABC]){5}', t)
print(len(max(m, key=len)))
print(max(m, key=len))