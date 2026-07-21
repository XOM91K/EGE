import re
s = open(r'C:\Users\Zarif\Downloads\153_1 (15).txt').readline()
m = re.findall(r'(?:PNO|NPO)+', s)
print(len(max(m, key=len)) / 3)