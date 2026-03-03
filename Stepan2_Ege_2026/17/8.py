l = [int(x) for x in open('8.txt')]
mn1 = max([d for d in l if str(d)[-1:] == '1'])
mn = []
for x in range(len(l) - 3):
    if (l[x]) < mn1 and (l[x + 1]) < mn1 and (l[x + 2]) < mn1 and (l[x + 3]) < mn1:
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
            mn.append((l[x]) + (l[x + 1]) + (l[x + 2]) + (l[x + 3]))
print(len(mn), min(mn))