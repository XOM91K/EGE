l = [[int(d) for d in x.split()] for x in open('19.txt')]
l2 = []
for x in range(len(l)):
    l2.append([l[x][0], x + 1, 'ш'])
    l2.append([l[x][1], x + 1, 'о'])
l2 = sorted(l2, key=lambda d: d[0])
mesta = [-1] * 970
i = 0
j = -1
for x in l2:
    if x[1] not in mesta:
        if x[-1] == 'ш':
            mesta[i] = x[1]
            print(x[1])
            i += 1
        else:
            mesta[j] = x[1]
            print(x[1])
            j -= 1
print(mesta.index(503))