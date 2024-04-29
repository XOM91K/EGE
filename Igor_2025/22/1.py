l = [x.strip().split('\t') for x in open('1.txt')]
sl = {}
for x in l:
    if int(x[0]) not in sl:
        sl[int(x[0])] = []
    sl[int(x[0])] = [int(x[1]), [int(d) for d in x[2].split(';')]]
print(sl)
for x in sl:
    if sl[x][1][0] == 0:
        sl[x].append(sl[x][0])
    else:
        mx = 0
        for y in sl[x][1]:
            mx = max(mx, sl[y][-1])
        sl[x].append(sl[x][0] + mx)
mx2 = 0
for x in sl:
    mx2 = max(mx2, sl[x][-1])
print(mx2)