l = [x for x in open('20.txt')]
uch = sorted([int(x) for x in l[:199154]])
sn = [[int(d) for d in x.split()] for x in l[199154:]]
sn = sorted(sn, key=lambda d: (d[1], -d[0]))
sns = []
i = 0
j = 0
for x in uch:
    for y in sn:
        if y[0] >= x:
            sns.append(y)
            break
print(uch)
print(sn)
print(sum([d[1] for d in sns]))
print(max([d[0] for d in sns]))