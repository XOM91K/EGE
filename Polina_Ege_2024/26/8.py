l = [[int(d) for d in x.split()] for x in open('8.txt')]
l = sorted(l, key=lambda d: d[0] + d[1])
print(l)
ct_tasks = []
ball = 8
time_end = 0
for x in l:
    if x[0] >= time_end:
        time_end = x[0] + x[1]
        ct_tasks.append([x[0], x[1]])
print(len(ct_tasks) * ball)
mx_rzn = 0
for x in range(len(l) - 1, -1, -1):
    if l[x][0] >= sum(ct_tasks[-2]):
        mx_rzn = max(mx_rzn, ct_tasks[-1][0] - l[x][0])
print(ct_tasks[-1][0] - mx_rzn)
