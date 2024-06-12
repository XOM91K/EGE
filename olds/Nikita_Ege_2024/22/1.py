sl = {}
l = [x.split('\t') for x in open('1.txt')]
for x in l:
    if int(x[0]) not in sl:
        sl[int(x[0])] = []
    sl[int(x[0])] = [int(x[1]), [int(d) for d in x[2].split(';')]]
for x in sl:
    if sl[x][1][0] == 0:
        sl[x].append(sl[x][0])
    else:
        mx = 0
        for y in sl[x][1]:
            mx = max(mx, sl[y][-1])
        sl[x].append(mx + sl[x][0])
mx = 0
for x in sl:
    mx = max(mx, sl[x][-1])
print(mx)