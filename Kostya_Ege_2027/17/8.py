l = [int(x) for x in open('8.txt')]
otr = sum([d for d in l if d < 0])
mx = []
for x in range(len(l) - 2):
    tr = [l[x], l[x + 1], l[x + 2]]
    if min(tr) + max(tr) > otr:
        mx.append((sum(tr)))
print(len(mx), max(mx))