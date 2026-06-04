a = [[int(d) for d in x.split()] for x in open('21.txt')]
b = []
b.append(a[0])
for e in a:
    if e not in b:
        b.append(e)
b = sorted(b)
cm = 0
c = 0
i = 0
while i <= 1440:
    for e in b:
        if i in e:
            c = 0
            break
        cc = 1
    if cc == 1:
        c += 1
    if c > cm:
        cm = c
    i += 1
print(cm)
mx = []
for e in b:
    mx.append(e[1])
mx = sorted(mx)
print(max(mx[-2], b[-1][1]))