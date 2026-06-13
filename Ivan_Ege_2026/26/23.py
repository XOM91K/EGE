l = [[int(d) for d in x.split()] for x in open('23.txt')]
l = sorted(l)
comps = []
ct = 0
for x in range(100):
    comps.append([0, 0])
for x in l:
    for y in range(len(comps)):
        if x[0] > comps[y][0]:
            comps[y][0] = x[1]
            t = x[1] - x[0]
            comps[y][1] += t * (t + 1) // 2
            ct += 1
            break
print(ct, max(comps, key=lambda d: d[1])[1])