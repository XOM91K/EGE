import re
s = open(r'C:\Users\Zarif\Downloads\1566_1.txt').readline()
m = re.findall(r'(?:[0-9][0-9][A-C])+',s)
print(len(max(m, key = len)))