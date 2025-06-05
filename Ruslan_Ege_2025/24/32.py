import re
s = open(r'C:\Users\Zarif\Downloads\1437_1 (2).txt').readline()
m = re.findall(r'[1-9A-Y]*Z[0-9A-Y]*Z[0-9A-Y]*Z[0-9A-Y]*Z[0-9A-Y]*', s)
for x in m:
    if len(x) > 0 and int(x, 36) % 36 == 0 and len(x) > 400:
        print(x)
        print(len(x))