# 999
l = [int(x) for x in open('3.txt')]
mn = min([x for x in l if x % 3 == 0])
mx = max([x for x in l if str(x)[-1] == '3'])
ct =0
mn2 = []
for x in range(len(l) - 1):
    k = 0
    if l[x + 1] >= mn and l[x + 1] <= mx:
        k += 1
    if l[x] >= mn and l[x] <= mx:
        k += 1
    if k == 1:
       ct += 1
       mn2.append(l[x] ** 2 + l[x + 1] ** 2)
print(ct, min(mn2))
