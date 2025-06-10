l = sorted([[int(d) for d in x.split()] for x in open('18.txt')])
M = 6661
K = 99906
p = [i + 1 for i in range(K)]
r = 0
u = p.copy()
sl = {}
rp = 0
print(l)
for i in l:
    if i[0] == r:
        rp = i[0]
    else:
        sl[rp] = u.copy()
        rp = i[0]
        r = i[0]
    u.remove(i[1])
sl[rp] = u.copy()
for z in sl:
    if len(sl[z]) >= 2:
        print(z, sl[z])