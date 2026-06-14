import re
s = open(r'C:\Users\Zarif\Downloads\24 (36).txt').readline().replace('BC', '#')
m = re.findall(r'(?=((?:[^#]*#){180}[^#]*))', s)
print(len(max(m, key=len)) + 180 + 2)