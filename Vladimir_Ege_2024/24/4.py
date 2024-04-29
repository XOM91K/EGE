import re
s = open('4.txt').readline()
m = re.findall(r"(?:[123]{2}[ABC])+", s)
print(len(max(m, key=len)) // 3)
print(max(m, key=len))