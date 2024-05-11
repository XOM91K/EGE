l = [int(x) for x in open('2.txt')]
mx = 0
ct = 0
mx121 = max([d for d in l if str(d)[-3:] == '121'])
for x in range(len(l) - 2):
    k = 0
    if len(str(abs(l[x]))) == 4 and l[x] % 2 == 0:
        k += 1
    if len(str(abs(l[x + 1]))) == 4 and l[x + 1] % 2 == 0:
        k += 1
    if len(str(abs(l[x + 2]))) == 4 and l[x + 2] % 2 == 0:
        k += 1
    if k <= 1 and (l[x] + l[x + 1] + l[x + 2]) <= mx121:
        ct += 1
        mx = max(mx, l[x] + l[x + 1] + l[x + 2])

print(ct, mx)