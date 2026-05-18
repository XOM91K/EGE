l = [[int(d) for d in x.split()] for x in open('15.txt')]
l = sorted(l)
sl = {}
for x in l:
    if x[0] not in sl:
        sl[x[0]] = []
    sl[x[0]].append(x[1])
mx_ct = []
for x in sl:
    ct = 1
    for y in range(len(sl[x]) - 1):
        if sl[x][y + 1] - sl[x][y] == 1:
            ct += 1
            mx_ct.append(ct)
            if ct == 14:
                print(x)
        else:
            ct = 1
print(max(mx_ct))