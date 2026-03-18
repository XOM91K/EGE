l = [int(x) for x in open('11.txt')]
mx17 = max([d for d in l if str(d)[-2:] == '17'])
mx = []
for x in range(len(l) - 2):
    k = 0
    if len(str(abs(l[x]))) == 4:
        k += 1
    if len(str(abs(l[x + 1]))) == 4:
        k += 1
    if len(str(abs(l[x + 2]))) == 4:
        k += 1
    if k == 2:
        k2 = 0
        if l[x] % 5 == 0:
            k2 += 1
        if l[x + 1] % 5 == 0:
            k2 += 1
        if l[x + 2] % 5 == 0:
            k2 += 1
        if k2 >= 1:
            if l[x] + l[x + 1] + l[x + 2] > mx17:
                mx.append(l[x] + l[x + 1] + l[x + 2])
print(len(mx), max(mx))