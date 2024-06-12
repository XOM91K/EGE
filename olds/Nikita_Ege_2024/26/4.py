l = sorted([[int(d) for d in x.split()] for x in open('4.txt')])
zn = -1
sm = 0
ct = 0
for x in l:
    if x[0] - zn > 1:
        sm += ((x[0] - 1) - zn)
        ct += 1
    zn = max(zn, x[1])
if (1439 - (zn + 1)) > 1:
    ct += 1
print(ct, sm + ((1439 - (zn + 1)) + 1))