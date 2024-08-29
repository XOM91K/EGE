l = [[int(d) for d in x.split()] for x in open('11.txt')]
ct = 0
for x in l:
    ch = 0
    nch = 0
    if x[0] % 2 == 0:
        ch += x[0]
    else:
        nch += x[0]
    if x[1] % 2 == 0:
        ch += x[1]
    else:
        nch += x[1]
    if x[2] % 2 == 0:
        ch += x[2]
    else:
        nch += x[2]
    if x[3] % 2 == 0:
        ch += x[3]
    else:
        nch += x[3]
    if x[4] % 2 == 0:
        ch += x[4]
    else:
        nch += x[4]
    if (len(set(x)) == 4 and nch <= ch) or (len(set(x)) != 4 and nch > ch):
        ct += 1
print(ct)