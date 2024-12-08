l = [int(x) for x in open('3.txt')]
mn_ch = min([d for d in l if d % 2 == 0])
ct = 0
mn = []
for x in range(len(l) - 2):
    k = 0
    if l[x] % 2 == 0:
        k += 1
    if l[x + 2] % 2 == 0:
        k += 1
    if k == 1:
        if l[x + 1] % mn_ch == 0:
            ct += 1
            mn.append(l[x] + l[x + 2])
print(ct, min(mn))