l = [[int(d) for d in x.split()] for x in open('11.txt')]
for x in range(len(l)):
    l[x].append(sum(l[x][1:-1]))
l = sorted(l, key=lambda d: (-d[-1], -d[-2], d[0]))
k = 0
for x in l:
    k += 1
    print(k, x)