l = [[int(d) for d in x.split()] for x in open('13.txt')]
l = sorted(l, key=lambda d: (d[1], d[1] - d[0]))
k = [0] * 500
ct = 0
for x in l:
    for y in range(len(k)):
        if x[0] > k[y]:
            k[y] = x[1]
            ct += 1
            print(y + 1)
            break
print(l[:20])
print(ct)