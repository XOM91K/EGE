import re
s = open(r'C:\Users\Zarif\Downloads\24 (42).txt').readline()
s = s.replace('EGE', '#').replace('2026', '@')
m = re.findall(r'(?=(#(?:[^#@]*@)+[^#@]*#))', s)
print(len(max(m, key=len)) + 3)