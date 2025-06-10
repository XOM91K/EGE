l = [int(x) for x in open('8.txt')]
mn = min([d for d in l if d % 3 == 0])
mx = max([d for d in l if str(d)[-1] == '3'])
ct = 0
mn_sm = []
for x in range(len(l) - 1):
    k = 0
    if (l[x] >= mn and l[x] <= mx):
        k += 1
    if (l[x + 1] >= mn and l[x + 1] <= mx):
        k += 1
    if k == 1:
        ct = ct + 1
        mn_sm.append(l[x] ** 2 + l[x + 1] ** 2)
print(ct, min(mn_sm))