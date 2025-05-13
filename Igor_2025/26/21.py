l = [[int(d) for d in x.split()] for x in open('21.txt')]
l = sorted(l)

K = 6661
m = {x for x in range(1, K + 1)}
print(m)
sl = {}
for x in l:
    if x[1] in m:
        m.remove(x[1])
    sl[x[0]] = m.copy()
for x in sl:
    sl[x] = sorted(sl[x])
    for y in range(len(sl[x]) - 1):
        if sl[x][y + 1] - sl[x][y] == 1:
            sl[x].append(['yes', sl[x][y]])
            break
    print(x, sl[x][-1])
