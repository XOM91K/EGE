l = [[int(d) for d in x.split()] for x in open('26.txt')]
yach = []
for x in range(102):
    yach.append([l[x][0], x + 1, 0])
yach = sorted(yach, key=lambda d: (d[0], d[1]))
print(yach)
print(yach)
sm_sum = 0
for x in sorted(l[102:], key=lambda d: d[0]):
    if x[0] <= 900:
        for y in range(len(yach)):
            if x[0] >= yach[y][-1]:
                print(yach[y][1])
                yach[y][-1] = x[0] + x[1]
                sm_sum += yach[y][0]
                break
print(sm_sum)