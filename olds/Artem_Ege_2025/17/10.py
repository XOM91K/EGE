a = ([int(x) for x in open('10.txt')])
mx = max([x for x in a if str(x)[-1] == '7'])
b = []
ct2 = 0
for i in range(len(a) - 2):
    k = 0
    ct = 0
    if a[i] % 2 != 0:
        k += 1
    if a[i + 1] % 2 != 0:
        k += 1
    if a[i + 2] % 2 != 0:
        k += 1
    if a[i] > mx:
        ct += 1
    if a[i + 1] > mx:
        ct += 1
    if a[i + 2] > mx:
        ct += 1
    if k == 2 and ct == 1:
        ct2 += 1
        b.append(a[i])
        b.append(a[i + 1])
        b.append(a[i + 2])
print(ct2, sum(set(b)) / len(set(b)))
