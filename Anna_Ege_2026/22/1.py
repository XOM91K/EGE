l = [[d for d in x.split('\t')] for x in open('1.txt')]
sl = {}
for x in l:
    if int(x[0]) not in sl:
        sl[int(x[0])] = [int(x[1]), [int(d) for d in x[2].split(';')]]
for x in sl:
    mx = [0]
    if sl[x][1][0] != 0:
        for y in sl[x][1]:
            mx.append(sl[y][-1])
    mx = max(mx)
    sl[x].append(sl[x][0] + mx)
mx = []
for x in sl:
    mx.append(sl[x][-1])
print(max(mx))