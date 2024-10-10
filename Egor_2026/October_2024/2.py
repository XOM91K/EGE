c = ['abcfhi', 'hcd', 'bcgi', 'bdeg', 'aech',
     'baehi', 'defih', 'bdf', 'abcefhi', 'abceg']
c = [''.join(sorted(x)) for x in c]
n = int(input())
s = set()
for i in range(n):
    d = int(input())
    s = s.union(c[d])
s = ''.join(sorted(s))
for i in c:
    f = True
    for j in i:
        if j not in s:
            f = False
    if f:
        print(c.index(i))