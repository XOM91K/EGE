l = [[int(d) for d in x.split()] for x in open('10.txt')]
l = sorted(l)
sl = {}
for x in l:
    if x[0] not in sl:
        sl[x[0]] = []
    sl[x[0]].append(x[1])
for x in sl:
    sl[x] = len(set([d for d in sl[x] if d % 2 == 0]))
    if sl[x] > 20:
        print(x, sl[x])
