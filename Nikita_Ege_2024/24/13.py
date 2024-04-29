import re
s = open('13.txt').readline()
m = re.findall(r"Q(?:RSQ)+RS", s)
print(len(max(m, key=len)))