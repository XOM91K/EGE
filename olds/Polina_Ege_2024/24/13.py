import re
s = open(r'C:\Users\Zarif\Downloads\24 (5).txt').readline()
m = re.findall(r"(?:[AO][AO][CDF])+", s)
print(max(m, key=len))