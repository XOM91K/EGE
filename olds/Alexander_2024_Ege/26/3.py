s = 10000
d = s
l = sorted([int(x) for x in open('3.txt')])
ct = 0
r = []
print(l)
for x in range(len(l) - 1, -1, -1):
    if 180 <= l[x] <= 200:
        s -= l[x]
        ct += 1
for x in range(len(l)):
    if not(180 <= l[x] <= 200) and s - l[x] >= 0:
        s -= l[x]
        r.append(l[x])
        ct += 1
    else:
        break
s += l[x - 1]
r = r[:-1]
for x in range(len(l) - 1, -1, -1):
    if not(180 <= l[x] <= 200) and s - l[x] >= 0:
        s -= l[x]
        if len(r) == 0:
            break
        s += r[-1]
        del r[-1]

print(ct, d - s)