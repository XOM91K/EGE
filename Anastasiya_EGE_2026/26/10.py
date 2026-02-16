l = [[int(d) for d in x.split()] for x in open('10.txt')]
k = 0
l = sorted(l, key=lambda d: (-sum(d[1:]), -d[-1], d[0]))
for x in l:
    k += 1
    x.append(sum(x[1:]))
    print(k, x)
ct = 0
for x in l:
    if x[-1] == 279:
        ct += 1
print(ct)