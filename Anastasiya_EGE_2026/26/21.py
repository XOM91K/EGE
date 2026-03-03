l = [[int(d) for d in x.split()] for x in open('21.txt')]
ll = []
for x in range(len(l)):
    ll.append([l[x][0], x + 1, 'ш'])
    ll.append([l[x][1], x + 1, 'о'])
ll = sorted(ll, key=lambda d: d[0])
mesta = [0] * 997
lt = 0
rt = -1
for x in ll:
    if x[1] not in mesta:
        if x[-1] == 'ш':
            mesta[lt] = x[1]
            print(x[1])
            lt += 1
        else:
            mesta[rt] = x[1]
            print(x[1])
            rt -= 1
print(mesta.index(895))