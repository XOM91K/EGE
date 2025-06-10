l = sorted([[int(d) for d in x.split()] for x in open('9.txt')], reverse=True)
sl = {}
k = 12
for x in l:
    if x[0] not in sl:
        sl[x[0]] = []
    sl[x[0]].append(x[1])
for x in sl:
    sl[x] = sorted(sl[x])
    for i in range(len(sl[x]) - 1):
        if sl[x][i + 1] - sl[x][i] == k:
            print(x, sl[x][i] + 1)
            exit()