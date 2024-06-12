l = [int(x) for x in open('6.txt')]
k = 137
pr_l = [0] * (len(l) + 1)
for x in range(len(l)):
    pr_l[x + 1] = pr_l[x] + l[x]
sl = {}
for x in range(len(pr_l)):
    if pr_l[x] % k not in sl:
        sl[pr_l[x] % k] = []
    sl[pr_l[x] % k].append(x)
mx_sm = 0
mx_ln = 0
for x in sl:
    mx_sm = max(mx_sm, pr_l[sl[x][-1]] - pr_l[sl[x][0]])
for x in sl:
    if pr_l[sl[x][-1]] - pr_l[sl[x][0]] == mx_sm:
        mx_ln = max(mx_ln, sl[x][-1] - sl[x][0])
print(mx_ln)