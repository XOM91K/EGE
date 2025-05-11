d = [[int(d) for d in x.split()] for x in open('11.txt')]
l = sorted(d)
sl = {}
for x in l:
    if x[0] not in sl:
        sl[x[0]] = []
    sl[x[0]].append(x[1])
ct = 1
for x in sl:
    sl[x] = sorted(set(sl[x]))
    ct_l = 0
    sl[x].append(10 ** 7)
    for y in range(len(sl[x]) - 1):
        if sl[x][y + 1] - sl[x][y] == 1:
            ct += 1
        else:
            if ct >= 3:
                ct_l += 1
            ct = 1
    sl[x].append(ct_l)
mx_ln = 0
for x in sl:
    mx_ln = max(mx_ln, sl[x][-1])
for x in sl:
    if mx_ln == sl[x][-1]:
        print(x)
print(mx_ln)