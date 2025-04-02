l = [[int(d) for d in x.split()] for x in open('14.txt')]
l = sorted(l)
sl = {}
for x in l:
    if x[0] not in sl:
        sl[x[0]] = []
    sl[x[0]].append(x[1])
ct = 0
for x in sl:

    sl[x].append(1)
    sl[x].append(10000)
    sl[x] = sorted(set(sl[x]))
    for y in range(len(sl[x]) - 2):
        if sl[x][y + 1] - sl[x][y] - 1 == 5 and sl[x][y + 2] - sl[x][y + 1] - 1 == 5:
            ct += 1
            print(x)
print(ct)
#print(sl[5000])