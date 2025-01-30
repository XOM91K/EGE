l = [int(x) for x in open('10.txt')]
ms = []
mx8 = max([x for x in l if str(x)[0] == '8'])
for x in range(len(l) - 2):
    k = 0
    if str(abs(l[x]))[0] == '6':
        k += 1
    if str(abs(l[x + 1]))[0] == '6':
        k += 1
    if str(abs(l[x + 2]))[0] == '6':
        k += 1
    if k <= 1:
        if l[x] + l[x + 1] + l[x + 2] >= mx8:
            ms.append(l[x] + l[x + 1] + l[x + 2])
print(len(ms), min(ms))