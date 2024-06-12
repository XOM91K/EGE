s = open(r'C:\Users\Zarif\Downloads\24-230 (2).txt').readline()
s = s.split('K')
mx = 0
import fnmatch
for x in s:
    if x.isdigit() and fnmatch.fnmatch(x, '43??78???34'):
        mx = max(mx, int(x))
nch = 1
for x in str(mx):
    if int(x) % 2 != 0:
        nch *= int(x)
print(nch)