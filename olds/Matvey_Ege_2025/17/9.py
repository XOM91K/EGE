l = [int(x) for x in open('9.txt')]
mn = min([x for x in l if x % 2 == 0])
ct = 0
mn_pair = []
for x in range(len(l) - 2):
    if l[x + 1] % mn == 0:
        if (l[x] % 2 == 0 and l[x + 2] % 2 != 0) or (l[x] % 2 != 0 and l[x + 2] % 2 == 0):
            ct += 1
            mn_pair.append(l[x] + l[x + 2])
print(ct, min(mn_pair))