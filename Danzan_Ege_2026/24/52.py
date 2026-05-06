import re
s = open(r'C:\Users\Zarif\Downloads\1696_1 (1).txt').readline()
m = re.findall(r'(?:\([1-9]+\d*[12346789][+-][1-9]+\d*[05]\))+', s)
print(max(m, key=len), len(max(m, key=len)))