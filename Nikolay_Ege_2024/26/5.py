l = [[int(d) for d in x.split()] for x in open('5.txt')]
sl = {}
for x in l:
    if x[0] not in sl:
        sl[x[0]] = []
    sl[x[0]].append(x[1])
print(sl)
mx_ryad = 0
for x in sl:
    for y in range(len(sl[x]) - 1):
        if sl[x][y + 1] - sl[x][y] == 3:
            mx_ryad= max(mx_ryad, x)
for x in sl:
    for y in range(len(sl[x]) - 1):
        if sl[x][y + 1] - sl[x][y] == 3 and x == mx_ryad:
            print(sl[x][y] + 1)
            break
print(mx_ryad)