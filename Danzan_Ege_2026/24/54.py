import re
s = open(r'C:\Users\Zarif\Downloads\1171_1 (3).txt').readline()
m = re.findall(r'(?:[12349]+\d*[*-])+[12349]+\d*', s)
print(len(max(m, key=len)))