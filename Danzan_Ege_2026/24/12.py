import re
s = open(r'C:\Users\Zarif\Downloads\340_1 (11).txt').readline()
m = re.findall(r'(?:[^AEYUOI][AEYUOI])+[^AEYUOI]?', s)
print(max(m, key = len))
print(len(max(m, key = len)))