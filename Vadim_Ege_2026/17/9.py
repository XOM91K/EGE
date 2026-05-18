l = [int(x) for x in open('9.txt')]
c = []
m = max([x for x in l if str(x)[:2] == '45'])
for x in range(len(l) - 2):
    t = [l[x], l[x + 1], l[x + 2]]
    k = [i for i in t if i < 0]
    i = [y for y in t if str(y)[-2:] == '45']
    if str(sum(t))[-2:] == '45':
        i = sum(t)
    else:
        i = 100000
    if len(k) == 1:
        if sum(t) >= m:
            c.append(i)
print(len(c), min(c))
