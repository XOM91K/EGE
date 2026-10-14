l = [[int(d) for d in x.split()] for x in open('373.txt')]
l = sorted(l, key=lambda d: d[1])
confs = [l[0]]
ct = 1
for x in l:
    if ct % 3 == 0 and x[0] >= confs[-1][1] + 10:
        confs.append(x)
        ct += 1
    elif ct % 3 != 0 and x[0] >= confs[-1][1]:
        confs.append(x)
        ct += 1
k = 0
for x in confs:
    k += 1
    print(k, x)
print(len(confs))
for x in l:
    if x[0] > 1246:
        print(x)