k = 137
l = [int(x) for x in open('3.txt')]
pf = [0] * (len(l) + 1)
for x in range(len(l)):
    pf[x + 1] = pf[x] + l[x]
print(pf)
sl = {}
for x in range(len(pf)):
    if pf[x] % k not in sl:
        sl[pf[x] % k] = []
    sl[pf[x] % k].append(x)
mx_sm = 0
mx_ln = 0
for x in sl:
    if pf[sl[x][-1]] - pf[sl[x][0]] >= mx_sm:
        mx_sm = pf[sl[x][-1]] - pf[sl[x][0]]
        mx_ln = sl[x][-1] - sl[x][0]
print(mx_ln)