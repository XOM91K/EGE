l = [[int(d) for d in x.split()] for x in open('4.txt')]
l = sorted(l)[::-1]
sl = {}
for x in l:
    if x[0] not in sl:
        sl[x[0]] = []
    sl[x[0]].append(x[1])
for x in sl:
    sl[x] = sorted(sl[x])
    for y in range(1, 6662):
        pair = (y, y + 1)
        if y not in sl[x] and y + 1 not in sl[x]:
            can = True
            for z in sl:
                if (y in sl[z] or y + 1 in sl[z]) and z < x:
                    can = False
                    break
            if can:
                print(x, y)
                exit()
