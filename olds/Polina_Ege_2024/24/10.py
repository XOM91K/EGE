import re
s = open(r'C:\Users\Zarif\Downloads\24 (2).txt').readline()
m = re.split(r"XZZY", s)
print(len(max(m,key=len)) + 6)