import re
s = open(r'C:\Users\Zarif\Downloads\24_28765 (1).txt').readline()
s = s.replace('BC', '#')
m = re.findall(r'(?=((?:[^#]*#){180}[^#]*))', s)
print(len(min(m, key=len)) + 180 + 2)