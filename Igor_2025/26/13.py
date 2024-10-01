l = sorted([int(x) for x in open('13.txt')])
sml = sum(l)
ms = [False] * (sml + 1)
ms[0] = True
for x in l:
    for y in range(len(ms) - 1, -1, -1):
        ms[x] = ms[y] or ms[y - x]
print(ms)
print([x for x in range(len(ms))])
print(sml)