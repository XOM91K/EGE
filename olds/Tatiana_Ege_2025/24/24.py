#31.05.2025
import re
s = open(r'C:\Users\Zarif\Downloads\1437_1 (1).txt').readline()
m = re.findall(r'[^0](?:[^Z]*Z?){4}[^Z]*', s)
r = []
for x in m:
    if int(x, 36) % 36 == 0:
        r.append(len(x))
print(max(r))