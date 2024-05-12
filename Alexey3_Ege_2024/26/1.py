l = [[int(d) for d in x.split()] for x in open('1.txt')]
l = sorted(l, key=lambda d: d[1])
confs = [l[0]]
for x in l:
    if x[0] - confs[-1][1] >= 20:
        confs.append(x)
mx_rzn = 0
for x in range(len(l) - 1, -1, -1):
    mx_rzn = max(mx_rzn, l[x][0] - confs[-2][1])
print(len(confs), mx_rzn)