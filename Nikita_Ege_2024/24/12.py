import re
s = open(r'C:\Users\Zarif\Downloads\24_12254 (2).txt').readline()
m = re.findall(r"Q(?:RSQ)+RS", s)
print(len(max(m, key=len)))