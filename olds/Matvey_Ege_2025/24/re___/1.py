import re
s = open('1.txt').readline()
m = re.findall('X+', s)
print(len(max(m, key=len)))
# 14121010