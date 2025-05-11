l = [[int(d) for d in x.split()] for x in open('5.txt')]
n = len(l)
l2 = l.copy()
l = [x for x in l if 2 not in x[1:]]
l2 = [x for x in l2 if 2 in x[1:]]
l = sorted(l, key=lambda d: (-sum(d[1:]), d[0]))
l2 = sorted(l2, key=lambda d: (d.count(2), d[0]))
l = l.copy() + l2.copy()
d25 = l[:n // 4]
print(d25[-1][0])
print([x for x in l if x[1:].count(2) > 2][0][0])
