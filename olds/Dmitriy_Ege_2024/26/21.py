l = [[int(d) for d in x.split()] for x in open('21.txt')]
l = sorted(l, key=lambda d: d[1])
print(l)
time_end = 0
ct_confs = []
for x in l:
    if x[0] >= time_end:
        time_end = x[1]
        ct_confs.append([x[0], x[1]])
del ct_confs[-1]
mx_prv = 0
for x in range(len(l) - 1, -1, -1):
    mx_prv = max(mx_prv, l[x][0] - ct_confs[-1][-1])
print(len(ct_confs) + 1, mx_prv)