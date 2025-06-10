l = sorted([[int(d) for d in x.split()] for x in open('12.txt')])
sl = {}
for x in l:
    if x[0] not in sl:
        sl[x[0]] = []
    sl[x[0]].append(x[1])
mx_ct = 0
id = 10 ** 10
for x in sl:
    sl[x] = sorted(set(sl[x]))
    sl[x].append(10 ** 7)
    ct = 1
    for y in range(len(sl[x]) - 1):
        if sl[x][y + 1] - sl[x][y] == 1:
            ct += 1
        else:
            if ct >= mx_ct:
                mx_ct = ct
            ct = 1
for x in sl:
    sl[x] = sorted(set(sl[x]))
    sl[x].append(10 ** 7)
    ct = 1
    for y in range(len(sl[x]) - 1):
        if sl[x][y + 1] - sl[x][y] == 1:
            ct += 1
        else:
            if ct == mx_ct:
                print(x)
                id = min(id, x)
            ct = 1
print(id, mx_ct)