l = [int(x) for x in open('2.txt')]
mx = 0
ln = 0
sl = {}
pr_l = [0] * (len(l) + 1)
for x in range(len(l)):
    pr_l[x + 1] = pr_l[x] + l[x]
for x in range(len(pr_l)):
    if pr_l[x] % 43 not in sl:
        sl[pr_l[x] % 43] = []
    sl[pr_l[x] % 43].append(x)
for x in sl:
    mx = max(mx, pr_l[sl[x][-1]] - pr_l[sl[x][0]])
mn_ln = 10 ** 10
for x in sl:
    if pr_l[sl[x][-1]] - pr_l[sl[x][0]] == mx:
        mn_ln = min(mn_ln, sl[x][-1] - sl[x][0])
print(mn_ln)