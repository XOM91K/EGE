l = [int(x) for x in open('25.txt')]
mn3 = min([x for x in l if x % 3 == 0])
mx3 = max([x for x in l if str(x)[-1] == '3'])
print(mn3, mx3)
ct = 0
mn = []
for x in range(len(l) - 1):
    k = 0
    if l[x] >= mn3 and l[x] <= mx3:
        k += 1
    if l[x + 1] >= mn3 and l[x + 1] <= mx3:
        k += 1
    if k == 1:
        ct += 1
        mn.append(l[x] ** 2 + l[x + 1] ** 2)
print(ct, min(mn))