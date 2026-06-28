import re
s = open(r'C:\Users\Zarif\Downloads\24 (46).txt').readline()
s = s.replace('EGE', '#').replace('2026', '@')
m = re.findall(r'#(?:[^#@]+@)+[^#@]+#', s)
print(max(m, key=len))
print(len(max(m, key=len)) + 3 - 2 + 4)