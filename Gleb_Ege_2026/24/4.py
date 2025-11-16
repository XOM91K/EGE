import re
s = open('4.txt').readline()
m = re.findall(r'A+', s)
print(max(m, key=len))