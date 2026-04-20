l = [[int(d) for d in x.split()] for x in open('26.txt')]
l = sorted(l, key=lambda d: d[0])
yach = [-1] * 230
ct = 0
for x in l:
    for y in range(len(yach)):
        if x[0] > yach[y]:
            yach[y] = x[1]
            ct += 1
            print(y + 1)
            break

print(ct)