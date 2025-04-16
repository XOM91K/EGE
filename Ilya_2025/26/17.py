l = [[int(d) for d in x.split()] for x in open('17.txt')]
l = sorted(l)
sl = {}
for x in l:
    if x[1] not in sl:
        sl[x[1]] = []
    sl[x[1]].append(x[0])
for x in sl:
    sl[x] = sorted(sl[x])
    sl[x].append(min(sl[x]) - 1)
sl = list(sl.items())
for x in range(len(sl) - 1):
    print(sl[x])
    print(sl[x][0], min(sl[x][-1][-1], sl[x + 1][-1][-1]))
