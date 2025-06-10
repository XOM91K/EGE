l = [[int(d) for d in x.split()] for x in open('7.txt')]
l = sorted(l)
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
        if sl[x][y + 1] - sl[x][y] == 2:
            ct += 1
            mx_ct = max(mx_ct, ct)
            if ct == 26:
                print(x)
        else:
            ct = 1
print(mx_ct)