l = [[int(d) for d in x.split()] for x in open(r'11.txt')]
k = [0 for x in range(230)]
l = sorted(l, key=lambda d: d[1])
print(l)
ct = 0
for x in l:
    for y in range(len(k)):
        if x[0] > k[y]:
            k[y] = x[1]
            ct += 1
            print(y + 1)
            break
print(ct)