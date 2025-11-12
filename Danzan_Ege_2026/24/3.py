import re
s = open('3.txt').readline()
m = re.findall(r'[a-z]+@[a-z]+\.[a-z]+', s)
print(len(max(m, key=len)))