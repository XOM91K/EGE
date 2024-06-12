l = [int(x) for x in open('27_B.txt')]
pr_l = [0] * (len(l) + 1)
for x in range(len(l)):
    pr_l[x + 1] = l[x] + pr_l[x]
sl = {}
for x in range(len(pr_l)):
    if pr_l[x] % 137 not in sl:
        sl[pr_l[x] % 137] = []
    sl[pr_l[x] % 137].append(x)
mx_sm = 0
mx_ln = 0
for x in sl:
    if pr_l[sl[x][-1]] - pr_l[sl[x][0]] > mx_sm:
        mx_sm = pr_l[sl[x][-1]] - pr_l[sl[x][0]]
for x in sl:
    if pr_l[sl[x][-1]] - pr_l[sl[x][0]] == mx_sm:
        mx_ln = max(mx_ln, sl[x][-1] - sl[x][0])
print(mx_ln)