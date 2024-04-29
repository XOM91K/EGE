#4921
l = [[int(d) for d in g.split()] for g in open('8.txt')]
sl = {}
for x in l:
    if x[0] not in sl:
        sl[x[0]] = []
    sl[x[0]].append(x[1])
mx_len = 0
for x in sl:
    ct = 1
    sl[x] = sorted(set(sl[x]))
    sl[x].append(10_000_000)
    for y in range(len(sl[x]) - 1):
        if sl[x][y + 1] - sl[x][y] == 2:
            ct += 1
        else:
            mx_len = max(mx_len, ct)
            if ct == 8:
                print(x)
            ct = 1
print(mx_len)