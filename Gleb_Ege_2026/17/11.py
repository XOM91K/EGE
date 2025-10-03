l = [int(x) for x in open('11.txt')]
mx7 = max([d for d in l if str(d)[-1] == '7'])
sra = []
mx = []
ct = 0
for x in range(len(l) - 2):
    k = 0
    if l[x] % 2 != 0:
        k += 1
    if l[x + 1] % 2 != 0:
        k += 1
    if l[x + 2] % 2 != 0:
        k += 1
    if k == 2:
        if (l[x] > mx7 and (l[x + 1] < mx7 and l[x + 2] < mx7)) or ((l[x] < mx7 and l[x + 1] < mx7) and l[x + 2] > mx7) or ((l[x] < mx7 and l[x + 2] < mx7) and l[x + 1] > mx7):
            ct += 1
            sra.append(l[x])
            sra.append(l[x + 1])
            sra.append(l[x + 2])
print(ct)
print(sum(set(sra)) / len(set(sra)))