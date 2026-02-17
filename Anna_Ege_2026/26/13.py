l = [[int(d) for d in x.split()] for x in open('13.txt')]
l = sorted(l, key=lambda d: (d[0], d[1]))
#sl = {1: 5, 100: 500, 'hello': 33, 'red': 'green'}
#sl = {40: [3, 4], 50: [72, 124, 126, 126, 128]}....
# sl = {}
# sl[2] = 3
# sl[2] = 5
# print(sl)
sl = {}
for x in l:
    if x[0] not in sl:
        sl[x[0]] = []
    sl[x[0]].append(x[1])
mx = []
for x in sl:
    ct = 1
    sl[x] = sorted(set(sl[x]))
    for y in range(len(sl[x]) - 1):
        if sl[x][y + 1] - sl[x][y] == 2:
            ct += 1
            mx.append(ct)
        else:
            ct = 1

for x in sl:
    ct = 1
    sl[x] = sorted(set(sl[x]))
    for y in range(len(sl[x]) - 1):
        if sl[x][y + 1] - sl[x][y] == 2:
            ct += 1
            if ct == max(mx):
                print(x)
        else:
            ct = 1
print(max(mx))