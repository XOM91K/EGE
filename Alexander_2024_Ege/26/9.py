l = [[int(d) for d in x.split()] for x in open('9.txt')]
sl = {}
M = 20
for x in range(M):
    sl[x + 1] = [0, []]
for x in l:
    for y in range(len(sl[x[2]][1])):
        if x[0] > sl[x[2]][1][y]:
            sl[x[2]][1][y] = 10 ** 9
            break
    else:
        sl[x[3]][1].append(x[0] + x[1])
        sl[x[2]][0] += 1
mx = 0
minuta = 0
for x in range(10000):
    ct = 0
    for y in l:
        if y[0] <= x <= y[0] + y[1]:
            ct += 1
    if ct > mx:
        mx = ct
        minuta = x
print(minuta)