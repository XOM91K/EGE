l = [[int(d) for d in x.split()] for x in open('12.txt')]
l = sorted(l, key=lambda d: (d[0], d[1]))
sl = {}
k = 3
for x in l:
    if x[0] not in sl:
        sl[x[0]] = []
    sl[x[0]].append(x[1])
print(sl)
mx_ln = []
for x in sl:
    sl[x] = sorted(set(sl[x]))
    sl[x].append(1000000)
    ln = 1
    lines = 0
    for y in range(len(sl[x]) - 1):
        if sl[x][y + 1] - sl[x][y] == 1:
            ln += 1
        else:
            if ln >= 5:
                lines += 1
            ln = 1
    mx_ln.append(lines)
print(max(mx_ln))
for x in sl:
    sl[x] = sorted(set(sl[x]))
    sl[x].append(1000000)
    ln = 1
    lines = 0
    for y in range(len(sl[x]) - 1):
        if sl[x][y + 1] - sl[x][y] == 1:
            ln += 1
        else:
            if ln >= 5:
                lines += 1
            ln = 1
    if lines == max(mx_ln):
        print(x)