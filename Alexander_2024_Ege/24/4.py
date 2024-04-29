import re
s = open(r'C:\Users\Zarif\Downloads\24_12254 (3).txt').readline()
m = re.findall(r"Q(?:RSQ)+RS", s)
print(max(m, key=len))
print(len(max(m, key=len)))