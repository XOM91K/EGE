l = [[int(d) for d in x.split()] for x in open('7.txt')]
for x in range(len(l)):
    l[x] = [l[x][0], l[x][1], x + 1]
l = sorted(l, key=lambda d: min(d[0], d[1]))
konv = [0] * len(l)
i = 0
j = -1
print(l[-1][-1])
for x in l:
    if min(x[0], x[1]) == x[0]:
        konv[i] = x[2]
        i += 1
    else:
        konv[j] = x[2]
        j -= 1
print(len(konv[:konv.index(l[-1][-1])]))