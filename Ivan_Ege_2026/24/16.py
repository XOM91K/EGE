import re
s = open('16.txt').readline()
m = re.findall(r'(?:BAC|CAB){24}', s)
print(max(m, key=len))
print(len(max(m, key=len)))