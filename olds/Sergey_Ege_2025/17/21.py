l = [int(x) for x in open("21.txt")]
ct = 0
sr = 0
mx = max([x for x in l if str(x)[-1] == "7"])
print(mx)
mx1 = 0
m = []
for x in range(len(l) - 2):
    k = 0
    if l[x] % 2 != 0:
        k += 1
    if l[x + 1] % 2 != 0:
        k += 1
    if l[x + 2] % 2 != 0:
        k += 1
    if k == 2:
        k1 = 0
        if l[x] > mx:
            k1 += 1
        if l[x + 1] > mx:
            k1 += 1
        if l[x + 2] > mx:
            k1 += 1
        if k1 == 1:
            ct += 1
            r = list(set([l[x], l[x + 1], l[x + 2]]))
            m.extend(r)

print(m)
print(ct, sum(m) / ct)