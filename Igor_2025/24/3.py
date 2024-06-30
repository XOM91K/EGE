import re
s = open('3.txt').readline()
m = re.findall('(?:BAC|CAB)+', s)
print(max(m, key=len))
print(m)