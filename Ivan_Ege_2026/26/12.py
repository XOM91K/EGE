l = [[int(d) for d in x.split()] for x in open('12.txt')]
l = sorted(l, key=lambda d: (d[1], -d[0]))
aud = 0
lections = []
for x in l:
    if x[0] >= aud:
        if len(lections) % 3 == 0 and len(lections) > 0 and x[0] < aud + 10:
            continue
        aud = x[1]
        lections.append(x)
print(lections[-3], lections[-2], lections[-1])
print(len(lections))
print(57 - 21)
for x in l:
    if x[0] > 1246:
        print(x)