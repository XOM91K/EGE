l = [[int(d) for d in x.split()] for x in open('28.txt')]
yach = sorted(l[:200], key=lambda d: (d[1], d[0]))
for y in range(len(yach)):
    yach[y].extend([0, 0, 0])
print(yach)
tvr = sorted(l[200:])
print(tvr)
# [102, 100, когда освободится: 0, сколько заработали: 0, сколько клиентов: 0]
for x in tvr:
    for y in range(len(yach)):
        if x[0] > yach[y][2]:
            yach[y][2] = x[1]
            yach[y][3] += yach[y][1] * (x[1] - x[0] + 1)
            yach[y][4] += 1
            break
print(max(yach, key=lambda d: d[3])[0], max(yach, key=lambda d: d[-1])[-1])