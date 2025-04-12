l = [[int(d) for d in x.split()] for x in open('14.txt')]
n = 8
#sr = sum([x[1] for x in l]) / n
sl = {}
for x in l:
    if x[0] not in sl:
        sl[x[0]] = [0]
    if x[2] == 0:
        sl[x[0]].insert(0, x[1])
    if x[2] == 1:
        sl[x[0]][-1] += 1
sl = list(sl.items())
sl = sorted(sl, key=lambda d: (-len(d[1]), -sum(d[1], len(d[1]))))
for x in sl:
    print(x)
#l = sorted(l, key=lambda d: (d[0], ))
#for x in l:
 #   print(x)