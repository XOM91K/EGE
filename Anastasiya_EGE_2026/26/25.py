l = [[int(d) for d in x.split()] for x in open('25.txt')]
l = sorted(l, key=lambda d: (d[0], d[1]))
yach = [0] * 10
ct = 0
for x in l:
    for y in range(len(yach)):
        if x[0] > yach[y]:
            yach[y] = x[1]
            ct += 1
            print(y + 1)
            break
print(ct * 71)