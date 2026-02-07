import collections
s = open('45.txt').readlines()
mxQ = 0
for x in s:
    mxQ = max(mxQ, x.count('Q'))
for x in s:
    if x.count('Q') == mxQ:
        print(collections.Counter(x))
s = open('45.txt').read()
print(s.count('C'))