f = [[int(d) for d in x.split()] for x in open('15.txt')]
sl = {}
for x in f:
    if x[0] not in sl:
        sl[x[0]] = []
    sl[x[0]].append(x[1])
mx_z = 0
l = []
for x in sl:
    sl[x] = sorted(set(sl[x]))
    ln = 1
    for y in range(len(sl[x]) - 1):
        if sl[x][y + 1] - sl[x][y] == 1:
            ln += 1
            mx_z = max(mx_z, ln)
            if ln == mx_z:
                l.append(x)
            elif ln >= mx_z:
                l = [x]
        else:
            ln = 1
print(mx_z, min(l))