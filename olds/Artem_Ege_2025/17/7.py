l = [int(x) for x in open('7.txt')]
mx1 = max([x for x in l if str(x)[-1] == '1'])
mn = []
for x in range(len(l) - 3):
    k = 0
    if l[x] % 2 != 0:
        k += 1
    if l[x + 1] % 2 != 0:
        k += 1
    if l[x + 2] % 2 != 0:
        k += 1
    if l[x + 3] % 2 != 0:
        k += 1
    if k % 2 != 0:
        if l[x] < mx1 and l[x + 1] < mx1 and l[x + 2] < mx1 and l[x + 3] < mx1:
            mn.append(l[x] + l[x + 1] + l[x + 2] + l[x + 3])
print(len(mn), min(mn))