l = [int(x) for x in open('8.txt')]
mx = max([y for y in l if str(y)[-1] == '1'])
xy = []
for x in range(len(l)-3):
    k = 0
    if l[x] % 2 == 0:
        k += 1
    if l[x + 1] % 2 == 0:
        k += 1
    if l[x + 2] % 2 == 0:
        k += 1
    if l[x + 3] % 2 == 0:
        k += 1
    if k % 2 != 0:
        if l[x] < mx and l[x + 1] < mx and l[x + 2] < mx and l[x + 3] < mx:
            xy.append(l[x] + l[x + 1] + l[x + 2] + l[x + 3])
print(len(xy), min(xy))