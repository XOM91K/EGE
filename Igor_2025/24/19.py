import re
s = open('19.txt').readline()
m = re.findall(r"(?:[AOUIYE][^AOUIYE])+[AOUIYE]?|(?:[^AOUIYE][AOUIYE])+[^AOUIYE]?", s)
print(max(m, key=len))
print(len(max(m, key=len)))