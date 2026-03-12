l = [int(x) for x in open('4.txt')]
l = sorted(l, reverse=True)
blocks = []
inds = []
for x in range(len(l) - 1):
    if x not in inds:
        r = [l[x]]
        inds.append(x)
        for y in range(x + 1, len(l)):
            if r[-1] - l[y] >= 9 and y not in inds:
                r.append(l[y])
                inds.append(y)
        blocks.append(r)
print(blocks)
print(len(blocks), len(max(blocks, key=len)))