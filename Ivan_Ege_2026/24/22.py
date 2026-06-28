import re
s = open(r'C:\Users\Zarif\Downloads\24 (44).txt').readline()
s = s.replace('EGE', '#')
m = re.findall(r'#([^#]*2026[^#]*)#', s)
#print(max(m, key=len))
print(len(max(m, key=len)))