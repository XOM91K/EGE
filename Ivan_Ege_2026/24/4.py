import re
s = open(r'C:\Users\Zarif\Downloads\1265_1 (3).txt').readline()
m = re.findall(r'(?:[789]\d*|0)(?:[-*](?:[789]\d*|0))+', s)
print(len(max(m, key=len)))