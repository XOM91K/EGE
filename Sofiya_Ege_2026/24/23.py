import re
a=open(r'C:\Users\Zarif\Downloads\989_1 (3).txt').readline()
match=re.findall('(?:[AEO][AEO][BCDF])+', a)
print(len(max(match, key=len)) / 3)