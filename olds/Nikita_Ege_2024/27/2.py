l = [int(x) for x in open('2.txt')]
mx = 0
ln = []

for i in range(len(l) - 1):
    ct = 0
    for j in range(i, len(l)):
        ct += l[j]
        if ct % 43 == 0:
            if ct >= mx:
                mx = ct
                ln.append([ct, j - i + 1])
print(sorted(ln))