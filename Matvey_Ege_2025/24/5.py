import re
s = open('175_1 (13).txt').readline()
m = re.findall(r'(?:O[^OF]*F?[^OF]*F?[^OF]*)+O', s)
print(len(max(m, key=len)))
print(m)