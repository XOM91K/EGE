l = [[int(d) for d in x.split()] for x in open('19.txt')]
yach = sorted(l[:200], key=lambda d: (d[1], d[0]))
yach = [d + [0, 0, 0] for d in yach]
print(yach)
tvr = sorted(l[200:])
print(yach)
print(tvr)
for x in tvr:
    for y in range(len(yach)):
        if x[0] > yach[y][2]:
            yach[y][2] = x[1]
            yach[y][3] += yach[y][1] * ((x[1] - x[0]) + 1)
            yach[y][4] += 1
            break
print(max(yach, key=lambda d: d[-2])[0])
print(max(yach, key=lambda d: d[-1])[-1])