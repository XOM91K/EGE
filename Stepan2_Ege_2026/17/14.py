l = [int(x) for x in open('14.txt')]
mx7 = max([d for d in l if str(abs(d))[-1] == '7'])
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
        k = 0
        if l[x] > mx7:
            k += 1
        if l[x + 1] > mx7:
            k += 1
        if l[x + 2] > mx7:
            k += 1
        if k == 1:
            ct += 1
            mx.append(l[x])
            mx.append(l[x + 1])
            mx.append(l[x + 2])
print(ct, sum(set(mx)) / len(set(mx)))