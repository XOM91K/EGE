l = [int(x) for x in open('10.txt')]
sr_ar = []
ct = 0
mx = 0
for x in l:
    if len(str(x)) == 4:
        sr_ar.append(x)
sr_ar = sum(sr_ar) / len(sr_ar)
for x in range(len(l) - 1):
    if (l[x] + l[x + 1]) not in l and (l[x] + l[x + 1]) < sr_ar:
        ct += 1
        mx = max(mx, sum(map(int, str(l[x]) + str(l[x + 1]))))
print(ct, mx)
