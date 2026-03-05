l = [[int(d) for d in x.split()] for x in open('16.txt')]
l = sorted(l, key=lambda d: (-(d[1] + d[2] + d[3]), -d[-1], d[0]))
for x in range(len(l)):
    l[x].append(l[x][1] + l[x][2] + l[x][3])
k = 0
for x in l:
    k += 1
    print(k, x)