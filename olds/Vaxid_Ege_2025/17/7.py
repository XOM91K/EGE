l = [int(x) for x in open( '7.txt' )]
mx = max([d for d in l if str(d)[-1] == '1' and len(str(abs(d))) == 4])
mn = min([d for d in l if len(str(abs(d))) == 2])
ct = 0
mx_pr = []
for x in range(len(l) - 2):
    k = 0
    if l[x] > mn ** 2:
        k = k + 1
    if l[x + 1] > mn ** 2:
        k = k + 1
    if l[x + 2] > mn ** 2:
        k = k + 1
    if k == 2:
        if (abs(l[x]) * abs(l[x + 1]) * abs(l[x + 2])) % mx == 0:
            ct += 1
            mx_pr.append(abs(l[x]) + abs(l[x + 1]) + abs(l[x + 2]))
print(ct, mx_pr)