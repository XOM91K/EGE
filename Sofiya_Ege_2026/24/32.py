import collections
l = [x for x in open(r'C:\Users\Zarif\Downloads\1606_1.txt')]
ctQ = 0
s = ''
for x in l:
    ctQ = max(ctQ, x.count('Q'))
for x in l:
    if ctQ == x.count('Q'):
        s = x.strip()
symbol = collections.Counter(s).most_common()[-1][0]
ctsym = 0
for x in l:
    ctsym += x.count(symbol)
print(symbol, ctsym)

