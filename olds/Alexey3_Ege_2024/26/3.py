l = [[int(d) for d in x.split()] for x in open('3.txt')]
#3230 
sl = {}
for x in l:
    if x[0] not in sl:
        sl[x[0]] = []
    sl[x[0]].append(x[1])
mx_cell = 0
for x in sl:
    sl[x] = sorted(sl[x])
    for y in range(len(sl[x]) - 1):
        if sl[x][y + 1] - sl[x][y] == 12:
            mx_cell = max(mx_cell, x)
for x in sl:
    if x == mx_cell:
        for y in range(len(sl[x]) - 1):
            if sl[x][y + 1] - sl[x][y] == 12:
                print(mx_cell, sl[x][y] + 1)
                exit()