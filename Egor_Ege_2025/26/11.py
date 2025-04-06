l = sorted([[int(d) for d in x.split()] for x in open('11.txt')])
sl = {}
for x in l:
    if x[0] not in sl:
        sl[x[0]] = []
    sl[x[0]].append(x[1])
mx_ct_lines = 0
ryad = 0
for x in sl:
    sl[x].append(10 ** 5)
    sl[x] = sorted(set(sl[x]))
    ct_lines = 0
    ct = 1
    for y in range(len(sl[x]) - 1):
        if sl[x][y + 1] - sl[x][y] == 1:
            ct += 1
        else:
            if ct >= 5:
                ct_lines += 1
            ct = 1
    if ct_lines >= mx_ct_lines:
        mx_ct_lines = ct_lines
        ryad = x
print(mx_ct_lines, ryad)