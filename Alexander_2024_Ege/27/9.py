l = [[int(d) for d in x.split()] for x in open('9.txt')]
n = 270
i = 0
r = [[d, 0] for d in range(1, n + 1)]
for x in l:
    r[x[0] - 1][1] = x[1]
sm_mn = 10 ** 10
print(r)
punkt = 0
for f in r:
    sm = 0
    for y in r:
        sm += abs(f[0] - y[0]) * y[1]
    if sm * 2 <= sm_mn:
        sm_mn = sm * 2
        punkt = f[0]
print(punkt)