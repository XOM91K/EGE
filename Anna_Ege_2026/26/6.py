m = 10000
start = m
l = sorted([int(x) for x in open('6.txt')])
# 310-320
r = []
for x in l:
    if 310 <= x <= 320:
        m -= x
        r.append(x)
for x in l:
    if m - x > 0:
        m -= x
        r.append(x)
l = sorted(l)[::-1]
print(len(r))
r = sorted([x for x in r if not(310 <= x <= 320)])[::-1]
d = r.copy()
for x in range(len(d)):
    m += d[x]
    for y in range(len(l)):
        if not(310 <= y <= 320) and m - l[y] >= 0:
            m -= l[y]
            d[x] = l[y]
            l[y] = 99999999999
            break
print(start - m)


