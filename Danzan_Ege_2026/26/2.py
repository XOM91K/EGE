l = [[int(d) for d in x.split()] for x in open('2.txt')]
l = sorted(l, key=lambda d: (d[1], d[0]))
confs_zal = 0
confs = []
for x in l:
    if x[0] - confs_zal >= 15:
        confs_zal = x[1]
        confs.append(x)
print(l)
print(confs)
print(len(confs))