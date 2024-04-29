l = [int(x) for x in open('3.txt')]
M = 950
N = 700
g = l[:N]
k = l[M - 1:]
k = sorted(k)
g = sorted(g)
print(g)
print(k)
ct = 0
mx = 0
for x in range(len(g)):
    for y in range(len(k)):
        if g[x] <= k[y]:
            k[y] = -1
            ct += 1
            mx = max(mx, g[x])
            break
print(ct, mx)