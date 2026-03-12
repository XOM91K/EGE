l = [[int(d) for d in x.split()] for x in open('17.txt')]
l = sorted(l, key=lambda d: (-sum(d[1:]), -sum([x for x in d[1:] if x > 0]), len([x for x in d[1:] if x != 0]), d[0]))
ob = len(l) // 3
k = 0
ct = 0
for d in l:
    k += 1
    if (-15, -15, 6) == (-sum(d[1:]), -sum([x for x in d[1:] if x > 0]), len([x for x in d[1:] if x != 0])):
        print(k, d, (-sum(d[1:]), -sum([x for x in d[1:] if x > 0]), len([x for x in d[1:] if x != 0])))
        ct += 1
print(ob, ct)