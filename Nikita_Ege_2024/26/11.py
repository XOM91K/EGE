l = [[int(d) for d in x.split()] for x in open('11.txt')]
l = [[l[x][0], l[x][1], x + 1] for x in range(len(l))]
l = sorted(l, key=lambda d: min(d[:-1]))
ans = [0] * len(l)
lf = 0
rt = -1
last_detal = 0
for x in range(len(l)):
    if min(l[x][:-1]) == l[x][0]:
        ans[lf] = l[x][2]
        lf += 1
    else:
        ans[rt] = l[x][2]
        rt -= 1
    last_detal = l[x][2]
print(last_detal, ans.index(last_detal))