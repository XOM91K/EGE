import re
a = open(r'C:\Users\Zarif\Downloads\989_1.txt').readline()
m = re.findall(r'(?:[AEO][AEO][BCDF])+',a)
print(len(max(m, key=len)) / 3)