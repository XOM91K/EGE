M = 20
l = sorted([[int(d) for d in g.split()] for g in open('7.txt')])
sl = {}
for x in range(1, 21):
    sl[x] = [0, []]
for x in l:
    for i, y in enumerate(sl[x[2]][-1]):
        if x[0] + 1 > y:
            sl[x[2]][-1][i] = 9 ** 9
            break
    else:
        sl[x[2]][0] += 1
    sl[x[3]][-1].append(x[0] + x[1])
for x in sl:
    print(x, sl[x][0])
#время старта в минутах, длительность в минутах, номер парковки старта и финиша
