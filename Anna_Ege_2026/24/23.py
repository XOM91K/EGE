import re
s = open(r'C:\Users\Zarif\Downloads\340_1 (5).txt').readline()
m = re.findall(r'(?:[^AEIOUY][AEIOUY])+[^AEIOUY]?',s)
print(len(max(m, key = len)))