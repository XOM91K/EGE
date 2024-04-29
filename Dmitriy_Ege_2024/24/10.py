import re
s = open(r'C:\Users\Zarif\Downloads\24_634_1 (1).txt').readline()
m = re.findall(r'K(43[0-9]{2}78[0-9]{3}34)K', s)
l = max(m, key=int)
nechet = 1
for p in l:
    if int(p) % 2 != 0:
        nechet *= int(p)
print(nechet)