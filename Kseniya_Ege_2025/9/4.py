l = [[int(d) for d in x.split()] for x in open('4.txt')]
ct = 0
for x in l:
    k = 0
    if len(set(x)) == 4:
        k += 1
    sm_ch = 0
    sm_nch = 0
    for y in range(0, 5):
        if x[y] % 2 == 0:
            sm_ch = sm_ch + x[y]
        else:
            sm_nch = sm_nch + x[y]
    if sm_nch > sm_ch:
        k += 1
    if k == 1:
        ct += 1
print(ct)