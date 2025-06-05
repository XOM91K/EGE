l = sorted([[int(d) for d in x.split()] for x in open('18.txt')])
sl = {}
for x in l:
    if x[0] not in sl:
        sl[x[0]] = []
    sl[x[0]].append(x[1])
mx = 0
for x in sl:
    sl[x] = sorted(set(sl[x]))
    ln = len([y for y in sl[x] if y % 2 == 0])
    mx = max(mx, ln)
for x in sl:
    sl[x] = len([y for y in sl[x] if y % 2 == 0])
    if sl[x] == mx:
        print(x)