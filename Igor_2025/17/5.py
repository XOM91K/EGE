l = [int(x) for x in open('5.txt')]
ct = 0
mx = 0
mx19 = max([i for i in l if str(i)[-2:] == '19'])
for i in range(len(l) - 2):
    k = 0
    if len(str(abs(l[i]))) == 4:
        k += 1
    if len(str(abs(l[i + 1]))) == 4:
        k += 1
    if len(str(abs(l[i + 2]))) == 4:
        k += 1
    if k == 2:
        if l[i] % 3 == 0 or l[i + 1] % 3 == 0 or l[i + 2] % 3 == 0:
            if l[i] + l[i + 1] + l[i + 2] > mx19:
                ct += 1
                mx = max(mx, l[i] + l[i + 1] + l[i + 2])
print(ct, mx)