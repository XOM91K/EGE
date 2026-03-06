l = [int(d) for d in open('18.txt')]
otr = sum([y for y in l if y < 0])
mx = []
for x in range(len(l) - 2):
    a = [l[x], l[x + 1], l[x + 2]]
    if max(a) * min(a) > otr:
        mx.append(sum(a))
print(len(mx), max(mx))