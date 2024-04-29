l = sorted([[int(d) for d in x.split()] for x in open('7.txt')], reverse=True)
sl = {}
k = 11
for x in l:
    if x[0] not in sl:
        sl[x[0]] = []
    sl[x[0]].append(x[1])
for x in sl:
    sl[x] = sorted(sl[x])
    for y in range(len(sl[x]) - 1):
        if sl[x][y + 1] - sl[x][y] == k + 1:
            print(x, sl[x][y] + 1)
            exit()