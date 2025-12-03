import re
s = open(r'C:\Users\Zarif\Downloads\328_1 (5).txt').readline()
s = s.replace('CD', '#')
m = re.finditer(r'(?=(D?(?:[^#]*#){50}[^#]*C?))', s)
ln = []
for x in m:
    if len(x.group(1)) == 7650:
        ln.append(len(x.group(1)))
        print(x.group(1))
print(max(ln) + 50+ 2)