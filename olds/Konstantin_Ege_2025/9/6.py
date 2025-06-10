l = [[int(d) for d in x.split()] for x in open('6.txt')]
ct = 0
for x in l:
    if len(set(x)) == 5:
        ch = nch = sm_ch = sm_nch = 0
        if x[0] % 2 == 0:
            ch += 1
            sm_ch += x[0]
        else:
            nch += 1
            sm_nch += x[0]
        if x[1] % 2 == 0:
            ch += 1
            sm_ch += x[1]
        else:
            nch += 1
            sm_nch += x[1]
        if x[2] % 2 == 0:
            ch += 1
            sm_ch += x[2]
        else:
            nch += 1
            sm_nch += x[2]
        if x[3] % 2 == 0:
            ch += 1
            sm_ch += x[3]
        else:
            nch += 1
            sm_nch += x[3]
        if x[4] % 2 == 0:
            ch += 1
            sm_ch += x[4]
        else:
            nch += 1
            sm_nch += x[4]
        if ch < nch:
            if sm_ch > sm_nch:
                ct += 1
print(ct)