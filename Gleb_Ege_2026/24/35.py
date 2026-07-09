import re
s = open(r'C:\Users\Zarif\Downloads\153_1 (14).txt').readline()
m = re.findall(r'(?:NPO|PNO)+', s)
print(len(max(m, key=len)) // 3)