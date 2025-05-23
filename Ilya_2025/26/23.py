l = [[int(d) for d in x.split()] for x in open('23.txt')]
ct = 0
l2 = []
for x in l:
    l2.append([x[0], sum(x[1:]), x[-1]])
l = l2[::]
l = sorted(l, key=lambda x: (-x[1], -x[2], x[0]))
n = 0
for x in l:
    ct += 1
    if x[1] == 279:
        n += 1
    print(ct, x)
print(n)