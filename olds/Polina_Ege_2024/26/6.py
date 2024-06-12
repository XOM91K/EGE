import collections
l = sorted([int(x) for x in open('6.txt')])
s = 99973
r = []
for i in l:
    if s - i >= 0 and l.count(i) > 1:
        s -= i
        r.append(i)
if r[-1] != r[-2]:
    s += r[-1]
    del r[-1]
l = l[::-1]
k = r.count(r[-1])
s2 = r.count(r[-1]) * r[-1] + s
for x in l:
    if l.count(x) > 1:
        if s2 - k * x >= 0:
            print(x)
            break
r = r[:-k]
print(collections.Counter(r).most_common()[0][0])