import collections
s = open('18.txt').readlines()
mxQ = 0
for x in s:
    x = x.strip()
    mxQ = max(mxQ, x.count('Q'))
for x in s:
    x = x.strip()
    if mxQ == x.count('Q'):
        print(x)
        print(collections.Counter(x))
