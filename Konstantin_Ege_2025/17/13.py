l = [int(x) for x in open('13.txt')]
mn_ch = min([x for x in l if x % 2 == 0])
ct = 0
mn_pair = []
for x in range(len(l) - 1):
    k = 0
    if l[x] % 2 == 0:
        k += 1
    if l[x + 1] % 2 == 0:
        k += 1
    if k == 1:
        if (max(l[x + 1], l[x]) - min(l[x], l[x + 1])) % mn_ch == 0:
            ct += 1
            mn_pair.append(l[x] + l[x + 1])
print(ct, min(mn_pair))