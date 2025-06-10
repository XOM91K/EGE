l = [int(x) for x in open('5.txt')]
mx7 = max([x for x in l if str(x)[-1] == '7'])
sr = []
ct_tr = 0
for x in range(len(l) - 2):
    nch = [i for i in [l[x], l[x + 1], l[x + 2]] if i % 2 != 0]
    if len(nch) == 2:
        k = 0
        if l[x] > mx7:
            k += 1
        if l[x + 1] > mx7:
            k += 1
        if l[x + 2] > mx7:
            k += 1
        if k == 1:
            sr.append(l[x])
            sr.append(l[x + 1])
            sr.append(l[x + 2])
            ct_tr += 1
print(ct_tr)
sr = set(sr)
print(sum(sr) / len(sr))
# nch = [i for i in [5, 500, 123] if i % 2 != 0]
# print(nch)