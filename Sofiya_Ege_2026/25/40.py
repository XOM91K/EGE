l = [int(x) for x in open('40.txt')]
ek = sorted(l[:900])
snk = sorted(l[900:])
print(ek)
print(snk)
j = 0
ct = 0
d = []
for i in range(len(ek)):
    while j != len(snk):
        if ek[i] <= snk[j]:
            ct += 1
            d.append([i, j])
            j += 1
            break
        j += 1
print(ct)
print(d[-1])
for y in range(len(ek) - 1, d[-1][0], -1):
    for x in range(d[-1][1], len(snk)):
        if ek[y] <= snk[x]:
            print(ek[y])
            exit()