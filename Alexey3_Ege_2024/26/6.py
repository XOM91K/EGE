l = [[int(d) for d in x.split()] for x in open('6.txt')]
l = sorted(l, key=sum)
tasks = [l[0]]
for x in l:
    if x[0] >= sum(tasks[-1]):
        tasks.append(x)
mn = 10 ** 10
for x in l:
    if x[0] >= sum(tasks[-2]) and x[0] < tasks[-1][0]:
        mn = min(mn, x[0])
print(len(tasks) * 8, mn)