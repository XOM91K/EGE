import collections
s = open('3.txt').readlines()
l = []
for d in s:
    sl = {}
    for x in range(len(d) - 1):
        if d[x] == 'X':
            if d[x + 1] not in sl:
                sl[d[x + 1]] = 0
            sl[d[x + 1]] += 1
    mx = 0
    for x in sl:
        if sl[x] > mx:
            mx = sl[x]
    for x in sl:
        if sl[x] == mx:
            l.append(x)
print(collections.Counter(l))