import re
s = open('1.txt').readline()
m = re.findall(r"X+", s)
print(len(max(m, key=len)))