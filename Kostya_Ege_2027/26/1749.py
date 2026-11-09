r = 199154
ry = [int(x) for x in open('1749.txt').readlines()[:r]]
sn = [[int(d) for d in x.split()] for x in open('1749.txt').readlines()[r:]]
sn = sorted(sn, key=lambda d: (d[1], -d[0]))
zak = []
mx_mosh = []
for x in ry:
    for y in sn:
        if y[0] >= x:
            zak.append(y[1])
            mx_mosh.append(y[0])
            break
print(ry)
print(sn)
print(sum(zak), max(mx_mosh))