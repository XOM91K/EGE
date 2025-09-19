import re
s = open(r'C:\Users\Zarif\Downloads\989_1 (1).txt').readline()
m = re.findall(r'(?:[AEO][AEO][BCDF])+', s)
print(len(max(m, key=len)) / 3)