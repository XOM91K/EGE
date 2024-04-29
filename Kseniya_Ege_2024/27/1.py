l = [int(x) for x in open('1.txt')]
print(l)
K = 144
M = 256
ct_posl = 0
for i in range(len(l)):
    sm = l[i]
    ct = 1
    for j in range(i + 1, len(l)):
        if K <= ct <= M:
            sm += l[j]
            if str(sm)[-2:] == '24':
                ct_posl += 1
        ct += 1
print(ct_po