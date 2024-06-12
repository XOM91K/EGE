l = [int(x) for x in open('18.txt')]
ln2 = []
ln4 = []
ct = 0
mx = 0
for y in l:
    if len(str(abs(y))) == 2:
        ln2.append(y)
    if len(str(abs(y))) == 4 and str(y)[-1] == '1':
        ln4.append(y)
print(min(ln2))
for x in range(len(l) - 2):
    k = 0
    if l[x] > min(ln2) ** 2:
        k += 1
    if l[x + 1] > min(ln2) ** 2:
        k += 1
    if l[x + 2] > min(ln2) ** 2:
        k += 1
    if k == 2:
        if (abs(l[x]) * abs(l[x + 1]) * abs(l[x + 2])) % max(ln4) == 0:
            ct += 1
            mx = max(mx, abs(l[x]) + abs(l[x + 1]) + abs(l[x + 2]))
print(ct, mx)

