l = [int(x) for x in open('3.txt')]
mx19 = max([x for x in l if str(x)[-2:] == '19'])
mx = []
ct = 0
for x in range(len(l) - 2):
    k = 0
    if len(str(l[x])) == 4:
        k += 1
    if len(str(l[x + 1])) == 4:
        k += 1
    if len(str(l[x + 2])) == 4:
        k += 1
    if k == 2:
        if l[x] % 3 == 0 or l[x + 1] % 3 == 0 or l[x + 2] % 3 == 0:
            if l[x] + l[x + 1] + l[x + 2] > mx19:
                mx.append(l[x] + l[x + 1] + l[x + 2])
                ct += 1
print(ct, max(mx))