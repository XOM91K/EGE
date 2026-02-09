import collections
s = open('29.txt').readlines()
mxQ = 0
for x in s:
    x = x.strip()
    mxQ = max(mxQ, x.count('Q'))
for x in s:
    if mxQ == x.count('Q'):
        print(collections.Counter(x))
ctC = 0
for x in s:
    ctC += x.count('C')
print(ctC)