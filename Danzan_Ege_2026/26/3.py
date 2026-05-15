l = [[int(d) for d in x.split()] for x in open('3.txt')]
l = sorted(l, key=lambda d: (d[0], d[1]))
ct = 0
mx_ct = []
for x in range(len(l) - 1):
    if l[x][0] == l[x + 1][0] and l[x + 1][1] - l[x][1] == 1:
        ct += 1
        if ct == 369:
            print(l[x][0])
        mx_ct.append(ct)
    else:
        ct = 1
print(max(mx_ct))