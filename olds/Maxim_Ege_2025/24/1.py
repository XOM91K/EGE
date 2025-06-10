import re
s = open(r'C:\Users\Zarif\Downloads\153_1 (7).txt').readline()
m = re.findall(r'(?:NPO|PNO)+', s)
print(max(m, key=len))
print(len(max(m, key=len)) / 3)