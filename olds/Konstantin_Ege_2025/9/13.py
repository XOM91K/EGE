l = [[int(d) for d in x.split()] for x in open('13.txt')]
ct = 0
for x in l:
    sm_ch = 0
    sm_nch = 0
    if x[0] % 2 == 0:
        sm_ch += x[0]
    else:
        sm_nch += x[0]
    if x[1] % 2 == 0:
        sm_ch += x[1]
    else:
        sm_nch += x[1]
    if x[2] % 2 == 0:
        sm_ch += x[2]
    else:
        sm_nch += x[2]
    if x[3] % 2 == 0:
        sm_ch += x[3]
    else:
        sm_nch += x[3]
    if x[4] % 2 == 0:
        sm_ch += x[4]
    else:
        sm_nch += x[4]
    if (len(set(x)) == 4 and sm_nch <= sm_ch) or (len(set(x)) != 4 and sm_nch > sm_ch):
        print(x)
        ct += 1
print(ct)