l = [x.strip().split('\t') for x in open('1.txt')]
l = [[int(x[0]), int(x[1]), list(map(int, x[2].split(';')))] for x in l]
sl = {}

for x in l:
    sl[x[0]] = [x[1], x[2]]
for x in sl:
    if len(sl[x][1]) == 1 and sl[x][1][0] == 0:
        sl[x].append(sl[x][0])
for x in sl:
    if not(len(sl[x][1]) == 1 and sl[x][1][0] == 0):
        mx_time = 0
        for y in sl[x][1]:
            mx_time = max(mx_time, sl[y][-1])
        sl[x].append(mx_time + sl[x][0])
mx = 0
for x in sl:
    mx = max(mx, sl[x][-1])
print(mx)