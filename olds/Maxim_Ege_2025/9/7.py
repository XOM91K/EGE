l = [[int(d) for d in x.split()] for x in open('7.txt')]
ct = 0
for x in l:
    k = 0
    nepovt = [] # [11,22,33,44,55]
    sm_ch = 0
    sm_nch = 0
    for y in x:
        if y % 2 == 0:
            sm_ch += y
        else:
            sm_nch += y
        if x.count(y) == 1:
            nepovt.append(y)
    # if (len(nepovt) == 3 and sm_nch <= sm_ch) or (len(nepovt) != 3 and sm_nch > sm_ch):
    #     print(x)
    #     ct += 1
    if len(nepovt) == 3:
        k += 1
    if sm_nch > sm_ch:
        k += 1
    if k == 1:
        ct += 1
print(ct)