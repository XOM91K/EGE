import re
l = open(r'C:\Users\Zarif\Downloads\153_1 (8).txt').readline()
m = re.findall(r'(?:NPO|PNO)+',l)
print(len(max(m, key = len)) // 3)
print(max(m))