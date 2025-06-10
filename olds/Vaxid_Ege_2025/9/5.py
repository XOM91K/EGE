l = [[int(d) for d in x.split()] for x in open('5.txt')]
ct = 0
for x in l:
    # [22, 22, 45, 46, 47]
    k = 0
    if len(set(x)) == 4:
        k += 1
    sm_ch = 0
    sm_nch = 0
    for y in range(len(x)):
        if x[y] % 2 == 0:
            sm_ch += x[y]
        else:
            sm_nch += x[y]
    if sm_nch > sm_ch:
        k += 1
    if k == 1:
        ct += 1
print(ct)