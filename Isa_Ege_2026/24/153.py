import re
s = open(r'C:\Users\Zarif\Downloads\153_1 (13).txt').readline()
print(len(s))
m = re.findall(r'(?:NPO|PNO)+', s)
print(max(m, key=len))
print(len(max(m, key=len)) // 3)