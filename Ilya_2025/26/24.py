l = sorted([[int(d) for d in x.split()] for x in open('24.txt')])
sl = {}
for x in l:
    if x[0] not in sl:
        sl[x[0]] = []
    sl[x[0]].append(x[1])
for x in sl:
    sl[x] = sorted(set(sl[x]))
    sl[x].append(1000000)
    lines = 0
    ct = 1
    for y in range(len(sl[x]) - 1):
        if abs(sl[x][y + 1] - sl[x][y]) == 1:
            ct += 1
        else:
            if ct >= 5:
                lines += 1
                ct = 1
    sl[x].append([lines])
for x in sl:
    if sl[x][-1][-1] > 8:
        print(x, sl[x][-1][-1])