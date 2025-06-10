import re
s = open(r'C:\Users\Zarif\Downloads\340_1 (1).txt').readline()
m = re.findall('(?:[AOEIUY][^AOEIUY])+[AOEIUY]?|(?:[^AOEIUY][AOEIUY])+[^AOEIUY]?', s)
print(len(max(m, key=len)))