l = [[int(d) for d in x.split()] for x in open('16.txt')]
mx = max(max(l, key=lambda d: d[1]))
seconds = [0] * mx
for x in l:
    seconds[x[0] - 1] += 1
    seconds[x[1] - 1] -= 1
pr_l = [0] * (len(seconds) + 1)
for x in range(len(seconds)):
    pr_l[x + 1] = pr_l[x] + seconds[x]
mx_exp = max(pr_l)
ct = 0
mx_seconds = 0
for x in pr_l:
    if x == mx_exp:
        ct += 1
        mx_seconds = max(mx_seconds, ct)
    else:
        ct = 0
print(mx_exp, mx_seconds)