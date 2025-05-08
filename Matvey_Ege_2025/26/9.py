l = [[int(d) for d in x.split()] for x in open('9.txt')]
b = []
for x in range(2):
    b.append([])
#
c = 0
mn_time = 100000
i = 0
print(l)
for x in l:
    for y in range(len(b)):
        if len(b[y]) == 0:
            c += 1
            b[y].append([x[0], x[0] + x[1]])
            if x[0] + x[1] < mn_time:
                mn_time = x[0] + x[1]
                i = y
            break
        elif x[0] < b[y][-1][1] and c == 2:
            b[i].append([x[0], x[0] + x[1]])
            if x[0] + x[1] < mn_time:
                mn_time = x[0] + x[1]
                i = y
            break
print(b)