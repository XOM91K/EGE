l = [[int(d) for d in x.split()] for x in open('6.txt')]
l = sorted(l)
sl = {}
# sl = {40: [3, 4], 50: [72, 124, 126, 126, 128], 60: [33, 33]}
for x in l:
    if x[0] not in sl:
        sl[x[0]] = []
    sl[x[0]].append(x[1])
mx_ct = []
for x in sl:
    sl[x] = sorted(set(sl[x]))
    ct = 1
    for y in range(len(sl[x]) - 1):
        if sl[x][y + 1] - sl[x][y] == 2:
            ct += 1
            if ct == 42:
                print(x)
            mx_ct.append(ct)
        else:
            ct = 1
print(max(mx_ct))