l = [int(x) for x in open('7.txt')]
c = []
m = sorted([x for x in l if x % 17 == 0 and x > 0])
m = m[0] + m[1]
print(m)
j = max([x for x in l if abs(x) % 100 == 69]) ** 2
for x in range(0, len(l) - 3):
    t = [l[x], l[x + 1], l[x + 2], l[x + 3]]
    k = 0
    g = 0
    o = 1
    for y in t:
        o *= y
        if len(str(abs(y))) == 3:
            k += 1
        if abs(y) % 18 == 0:
            g += 1
    if k == 2 and g == 1:
        if sum(t) % m == 0 and o <= j:
            c.append(sum(t) ** 2)
print(len(c), min(c))
