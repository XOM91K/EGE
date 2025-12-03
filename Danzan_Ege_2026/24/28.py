import re
s = open(r'C:\Users\Zarif\Downloads\1397_2 (8).txt').readline()
s = s.replace('RSQ', '#')
m = re.finditer(r'(?=((?:#[^#]*?){129}#[^Q#]+?))', s)
ln = []
for x in m:
    ln.append(len(x.group(1)))
print(min(ln) + 130 * 2)