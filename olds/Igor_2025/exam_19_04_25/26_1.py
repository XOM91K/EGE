l = [[int(d) for d in x.split()] for x in open('26.txt')]
sl = {}
for x in l:
    if x[0] not in sl:
        sl[x[0]] = []
    sl[x[0]].append(x[1])
mx_ct = 0
for x in sl:
    sl[x] = sorted(set(sl[x]))
    ct = 1
    for y in range(len(sl[x]) - 1):
        if abs(sl[x][y + 1] - sl[x][y]) == 2:
            ct += 1
            mx_ct = max(mx_ct, ct)
        else:
            ct = 1
d = []
for x in sl:
    sl[x] = sorted(set(sl[x]))
    ct = 1
    for y in range(len(sl[x]) - 1):
        if abs(sl[x][y + 1] - sl[x][y]) == 2:
            ct += 1
            if ct == mx_ct:
                d.append(x)
        else:
            ct = 1
print(min(d), mx_ct)