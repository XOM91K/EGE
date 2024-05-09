l = [[int(d) for d in x.split()] for x in open('22.txt')]
for x in range(len(l)):
    if l[x][0] == 0:
        l[x][0] = 1634515201
    if l[x][1] == 0:
        l[x][1] = 1634515200 + 604799
time = [0] * 604_800
for x in l:
    if 1634515200 <= x[0] <= 1634515200 + 604_800:
        time[x[0] - 1634515200] += 1
    if 1634515200 <= x[1] <= 1634515200 + 604_800:
        time[x[1] - 1634515200] -= 1
print(time[:10])
pr_time = [0] * (len(time) + 1)
for x in range(len(time)):
    pr_time[x + 1] = pr_time[x] + time[x]
mx = 0
for x in pr_time:
    mx = max(mx, x)
print(pr_time)