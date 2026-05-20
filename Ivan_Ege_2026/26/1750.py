l = [x.split() for x in open('1750.txt')]
r = sorted([[int(x) for x in d[:2]] for d in l if d[-1] == 'R'], key=lambda d: -d[1])
g = sorted([[int(x) for x in d[:2]] for d in l if d[-1] == 'G'], key=lambda d: -d[1])
b = sorted([[int(x) for x in d[:2]] for d in l if d[-1] == 'B'], key=lambda d: -d[1])
print(r)
print(g)
print(b)
i = 0
j = 0
bashni = []
for x in range(len(r)):
    bashni.append([r[x]])
    for y in range(i, len(g)):
        if r[x][1] - g[y][1] >= 2:
            bashni[-1].append(g[y])
            i = y + 1
            for z in range(j, len(b)):
                if g[y][1] - b[z][1] >= 2:
                    bashni[-1].append(b[z])
                    j = z + 1
                    break
            if len(bashni[-1]) == 3:
                break
            else:
                print(len(bashni) - 1, bashni[-2][1][0])
                exit()


# for i in r:
