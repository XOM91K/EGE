a = [[int(d) for d in x.split()] for x in open('22.txt')]
b = []
for e in a:
    if e[1]%2==0:
        b.append([e[0], 1])
    else:
        b.append([e[0], 0])
sl = {}
for e in b:
    if e[0] not in sl:
        sl[e[0]] = []
    sl[e[0]].append(e[1])
ww = []
for e in sl:
    ww.append([e, sum(sl[e])])
ww = sorted(ww, key = lambda x: (-x[1], x[0]))
print(ww)