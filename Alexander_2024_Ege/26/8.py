l = [[int(d) for d in x.split()] for x in open('8.txt')]
sl = {}
k = 5
for x in l:
    if x[0] not in sl:
        sl[x[0]] = []

    sl[x[0]].append(x[1])
ln = []
for x in sl:
    ct_ln = 0
    ct = 1
    sl[x] = sorted(set(sl[x]))
    sl[x].append(10 ** 10)
    for y in range(len(sl[x]) - 1):
        if sl[x][y + 1] - sl[x][y] == 1:
            ct += 1
        else:
            if ct >= k:
                ct_ln += 1
            ct = 1
    ln.append([ct_ln, x])
print(sorted(ln))