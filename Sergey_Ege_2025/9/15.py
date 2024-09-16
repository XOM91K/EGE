l = [[int(d) for d in x.split()] for x in open('15.txt')]
ct = 0
for x in l:
    l1 = x.copy()
    l2 = sorted(x.copy())
    if (l1[0] != l2[0] and l1[0] != l2[-1]) and (l1[-1] != l2[0] and l1[-1] != l2[-1]):
        if l2[2] - l2[1] > 0:
            if (l2[-1] - l2[0]) % (l2[2] - l2[1]) == 0:
                ct += 1
print(ct)